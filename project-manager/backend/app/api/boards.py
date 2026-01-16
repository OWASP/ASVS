"""
Boards API endpoints
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models import Board, BoardColumn, Project

boards_bp = Blueprint('boards', __name__)


@boards_bp.route('', methods=['GET'])
@jwt_required()
def get_boards():
    """Get all boards"""
    project_id = request.args.get('project_id', type=int)

    query = Board.query
    if project_id:
        query = query.filter_by(project_id=project_id)

    boards = query.order_by(Board.position).all()
    return jsonify([b.to_dict() for b in boards]), 200


@boards_bp.route('', methods=['POST'])
@jwt_required()
def create_board():
    """Create a new board"""
    data = request.get_json()

    if not data.get('project_id'):
        return jsonify({'error': 'project_id is required'}), 400
    if not data.get('name'):
        return jsonify({'error': 'Board name is required'}), 400

    project = Project.query.get_or_404(data['project_id'])

    board = Board(
        project_id=data['project_id'],
        name=data['name'],
        description=data.get('description'),
        view_type=data.get('view_type', 'kanban'),
        is_default=data.get('is_default', False),
        settings=data.get('settings', {})
    )

    # Set position
    max_position = db.session.query(db.func.max(Board.position)).filter_by(
        project_id=data['project_id']
    ).scalar() or 0
    board.position = max_position + 1

    db.session.add(board)
    db.session.flush()

    # Create columns based on view type or custom columns
    if data.get('columns'):
        for i, col_data in enumerate(data['columns']):
            column = BoardColumn(
                board_id=board.id,
                name=col_data['name'],
                status_mapping=col_data.get('status_mapping'),
                color=col_data.get('color', '#6B7280'),
                position=i,
                wip_limit=col_data.get('wip_limit')
            )
            db.session.add(column)
    else:
        board.create_default_columns()

    db.session.commit()
    return jsonify(board.to_dict()), 201


@boards_bp.route('/<int:board_id>', methods=['GET'])
@jwt_required()
def get_board(board_id):
    """Get a specific board"""
    board = Board.query.get_or_404(board_id)
    include_tasks = request.args.get('include_tasks', 'false').lower() == 'true'
    return jsonify(board.to_dict(include_tasks=include_tasks)), 200


@boards_bp.route('/<int:board_id>', methods=['PUT'])
@jwt_required()
def update_board(board_id):
    """Update a board"""
    board = Board.query.get_or_404(board_id)
    data = request.get_json()

    allowed_fields = ['name', 'description', 'view_type', 'is_default', 'position', 'settings']
    for field in allowed_fields:
        if field in data:
            setattr(board, field, data[field])

    # If setting as default, unset other defaults
    if data.get('is_default'):
        Board.query.filter(
            Board.project_id == board.project_id,
            Board.id != board.id
        ).update({'is_default': False})

    db.session.commit()
    return jsonify(board.to_dict()), 200


@boards_bp.route('/<int:board_id>', methods=['DELETE'])
@jwt_required()
def delete_board(board_id):
    """Delete a board"""
    board = Board.query.get_or_404(board_id)

    if board.is_default:
        return jsonify({'error': 'Cannot delete default board'}), 400

    db.session.delete(board)
    db.session.commit()
    return jsonify({'message': 'Board deleted'}), 200


# Column endpoints
@boards_bp.route('/<int:board_id>/columns', methods=['GET'])
@jwt_required()
def get_columns(board_id):
    """Get board columns"""
    board = Board.query.get_or_404(board_id)
    columns = board.columns.order_by(BoardColumn.position).all()
    return jsonify([c.to_dict() for c in columns]), 200


@boards_bp.route('/<int:board_id>/columns', methods=['POST'])
@jwt_required()
def create_column(board_id):
    """Create a new column"""
    board = Board.query.get_or_404(board_id)
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Column name is required'}), 400

    max_position = db.session.query(db.func.max(BoardColumn.position)).filter_by(
        board_id=board_id
    ).scalar() or 0

    column = BoardColumn(
        board_id=board_id,
        name=data['name'],
        status_mapping=data.get('status_mapping'),
        color=data.get('color', '#6B7280'),
        position=data.get('position', max_position + 1),
        wip_limit=data.get('wip_limit')
    )
    db.session.add(column)
    db.session.commit()

    return jsonify(column.to_dict()), 201


@boards_bp.route('/columns/<int:column_id>', methods=['PUT'])
@jwt_required()
def update_column(column_id):
    """Update a column"""
    column = BoardColumn.query.get_or_404(column_id)
    data = request.get_json()

    allowed_fields = ['name', 'status_mapping', 'color', 'position', 'wip_limit']
    for field in allowed_fields:
        if field in data:
            setattr(column, field, data[field])

    db.session.commit()
    return jsonify(column.to_dict()), 200


@boards_bp.route('/columns/<int:column_id>', methods=['DELETE'])
@jwt_required()
def delete_column(column_id):
    """Delete a column"""
    column = BoardColumn.query.get_or_404(column_id)

    # Check if column has tasks
    from app.models import Task
    task_count = Task.query.filter_by(
        board_id=column.board_id,
        status=column.status_mapping
    ).count()

    if task_count > 0:
        return jsonify({'error': f'Column has {task_count} tasks. Move them first.'}), 400

    db.session.delete(column)
    db.session.commit()
    return jsonify({'message': 'Column deleted'}), 200


@boards_bp.route('/<int:board_id>/columns/reorder', methods=['POST'])
@jwt_required()
def reorder_columns(board_id):
    """Reorder columns"""
    board = Board.query.get_or_404(board_id)
    data = request.get_json()

    if not data.get('column_ids'):
        return jsonify({'error': 'column_ids array is required'}), 400

    for i, column_id in enumerate(data['column_ids']):
        column = BoardColumn.query.filter_by(id=column_id, board_id=board_id).first()
        if column:
            column.position = i

    db.session.commit()
    return jsonify({'message': 'Columns reordered'}), 200
