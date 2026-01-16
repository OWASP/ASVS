"""
Tasks API endpoints
"""
from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Task, TaskDependency, Comment, Attachment, TimeEntry, Tag, TaskTag, Board

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('', methods=['GET'])
@jwt_required()
def get_tasks():
    """Get tasks with filtering"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 50, type=int)
    board_id = request.args.get('board_id', type=int)
    project_id = request.args.get('project_id', type=int)
    assignee_id = request.args.get('assignee_id', type=int)
    status = request.args.get('status')
    priority = request.args.get('priority')
    search = request.args.get('search')

    query = Task.query

    if board_id:
        query = query.filter_by(board_id=board_id)
    if project_id:
        query = query.join(Board).filter(Board.project_id == project_id)
    if assignee_id:
        query = query.filter_by(assignee_id=assignee_id)
    if status:
        query = query.filter_by(status=status)
    if priority:
        query = query.filter_by(priority=priority)
    if search:
        query = query.filter(Task.title.ilike(f'%{search}%'))

    pagination = query.order_by(Task.position).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'tasks': [t.to_dict() for t in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@tasks_bp.route('', methods=['POST'])
@jwt_required()
def create_task():
    """Create a new task"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('board_id'):
        return jsonify({'error': 'board_id is required'}), 400
    if not data.get('title'):
        return jsonify({'error': 'Task title is required'}), 400

    board = Board.query.get_or_404(data['board_id'])

    # Get max position for the board
    max_position = db.session.query(db.func.max(Task.position)).filter_by(
        board_id=data['board_id']
    ).scalar() or 0

    task = Task(
        board_id=data['board_id'],
        title=data['title'],
        description=data.get('description'),
        status=data.get('status', 'todo'),
        priority=data.get('priority', 'medium'),
        task_type=data.get('task_type', 'task'),
        assignee_id=data.get('assignee_id'),
        reporter_id=user_id,
        estimated_hours=data.get('estimated_hours', 0),
        position=data.get('position', max_position + 1),
        parent_id=data.get('parent_id'),
        custom_fields=data.get('custom_fields', {})
    )

    if data.get('start_date'):
        task.start_date = datetime.fromisoformat(data['start_date']).date()
    if data.get('due_date'):
        task.due_date = datetime.fromisoformat(data['due_date']).date()

    db.session.add(task)
    db.session.flush()

    # Add tags if provided
    if data.get('tags'):
        for tag_name in data['tags']:
            tag = Tag.query.filter_by(name=tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                db.session.add(tag)
                db.session.flush()
            task_tag = TaskTag(task_id=task.id, tag_id=tag.id)
            db.session.add(task_tag)

    # Add dependencies if provided
    if data.get('dependencies'):
        for dep_id in data['dependencies']:
            dep = TaskDependency(
                task_id=task.id,
                depends_on_id=dep_id,
                dependency_type=data.get('dependency_type', 'finish_to_start')
            )
            db.session.add(dep)

    db.session.commit()

    # Trigger automation if applicable
    from app.services.automation_engine import AutomationEngine
    engine = AutomationEngine()
    engine.trigger('task_created', task)

    return jsonify(task.to_dict()), 201


@tasks_bp.route('/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    """Get a specific task"""
    task = Task.query.get_or_404(task_id)
    include_comments = request.args.get('include_comments', 'false').lower() == 'true'
    return jsonify(task.to_dict(include_comments=include_comments)), 200


@tasks_bp.route('/<int:task_id>', methods=['PUT'])
@jwt_required()
def update_task(task_id):
    """Update a task"""
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    old_status = task.status

    allowed_fields = ['title', 'description', 'status', 'priority', 'task_type',
                      'assignee_id', 'estimated_hours', 'progress', 'position',
                      'parent_id', 'custom_fields', 'board_id']

    for field in allowed_fields:
        if field in data:
            setattr(task, field, data[field])

    # Handle date fields
    if 'start_date' in data:
        task.start_date = datetime.fromisoformat(data['start_date']).date() if data['start_date'] else None
    if 'due_date' in data:
        task.due_date = datetime.fromisoformat(data['due_date']).date() if data['due_date'] else None

    # Handle status change
    if data.get('status') == 'completed' and old_status != 'completed':
        task.completed_date = datetime.utcnow().date()
        task.progress = 100
    elif data.get('status') != 'completed' and old_status == 'completed':
        task.completed_date = None

    db.session.commit()

    # Trigger automations
    from app.services.automation_engine import AutomationEngine
    engine = AutomationEngine()
    engine.trigger('task_updated', task, changes={'old_status': old_status})

    if data.get('status') and data['status'] != old_status:
        engine.trigger('task_status_changed', task, changes={
            'old_status': old_status,
            'new_status': data['status']
        })

    return jsonify(task.to_dict()), 200


@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    """Delete a task"""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'}), 200


# Bulk operations
@tasks_bp.route('/bulk-update', methods=['POST'])
@jwt_required()
def bulk_update_tasks():
    """Bulk update multiple tasks"""
    data = request.get_json()

    if not data.get('task_ids') or not data.get('updates'):
        return jsonify({'error': 'task_ids and updates required'}), 400

    tasks = Task.query.filter(Task.id.in_(data['task_ids'])).all()

    for task in tasks:
        for field, value in data['updates'].items():
            if hasattr(task, field):
                setattr(task, field, value)

    db.session.commit()
    return jsonify({'message': f'Updated {len(tasks)} tasks'}), 200


@tasks_bp.route('/reorder', methods=['POST'])
@jwt_required()
def reorder_tasks():
    """Reorder tasks within a board/column"""
    data = request.get_json()

    if not data.get('task_orders'):
        return jsonify({'error': 'task_orders array required'}), 400

    for item in data['task_orders']:
        task = Task.query.get(item['id'])
        if task:
            task.position = item['position']
            if 'status' in item:
                task.status = item['status']

    db.session.commit()
    return jsonify({'message': 'Tasks reordered'}), 200


# Dependencies
@tasks_bp.route('/<int:task_id>/dependencies', methods=['GET'])
@jwt_required()
def get_dependencies(task_id):
    """Get task dependencies"""
    task = Task.query.get_or_404(task_id)
    return jsonify({
        'dependencies': [d.to_dict() for d in task.dependencies],
        'dependents': [d.to_dict() for d in task.dependents]
    }), 200


@tasks_bp.route('/<int:task_id>/dependencies', methods=['POST'])
@jwt_required()
def add_dependency(task_id):
    """Add a dependency"""
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    if not data.get('depends_on_id'):
        return jsonify({'error': 'depends_on_id is required'}), 400

    # Check for circular dependency
    depends_on = Task.query.get_or_404(data['depends_on_id'])

    # Simple circular check
    if depends_on.id == task.id:
        return jsonify({'error': 'Task cannot depend on itself'}), 400

    # Check if dependency already exists
    existing = TaskDependency.query.filter_by(
        task_id=task_id,
        depends_on_id=data['depends_on_id']
    ).first()
    if existing:
        return jsonify({'error': 'Dependency already exists'}), 409

    dep = TaskDependency(
        task_id=task_id,
        depends_on_id=data['depends_on_id'],
        dependency_type=data.get('dependency_type', 'finish_to_start'),
        lag_days=data.get('lag_days', 0)
    )
    db.session.add(dep)
    db.session.commit()

    return jsonify(dep.to_dict()), 201


@tasks_bp.route('/dependencies/<int:dep_id>', methods=['DELETE'])
@jwt_required()
def remove_dependency(dep_id):
    """Remove a dependency"""
    dep = TaskDependency.query.get_or_404(dep_id)
    db.session.delete(dep)
    db.session.commit()
    return jsonify({'message': 'Dependency removed'}), 200


# Comments
@tasks_bp.route('/<int:task_id>/comments', methods=['GET'])
@jwt_required()
def get_comments(task_id):
    """Get task comments"""
    task = Task.query.get_or_404(task_id)
    comments = task.comments.order_by(Comment.created_at.desc()).all()
    return jsonify([c.to_dict() for c in comments]), 200


@tasks_bp.route('/<int:task_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(task_id):
    """Add a comment"""
    user_id = get_jwt_identity()
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    if not data.get('content'):
        return jsonify({'error': 'Comment content is required'}), 400

    comment = Comment(
        task_id=task_id,
        author_id=user_id,
        content=data['content'],
        parent_id=data.get('parent_id'),
        mentions=data.get('mentions', [])
    )
    db.session.add(comment)
    db.session.commit()

    # Trigger automation and notifications
    from app.services.automation_engine import AutomationEngine
    engine = AutomationEngine()
    engine.trigger('comment_added', task, context={'comment': comment})

    return jsonify(comment.to_dict()), 201


# Time entries
@tasks_bp.route('/<int:task_id>/time-entries', methods=['GET'])
@jwt_required()
def get_time_entries(task_id):
    """Get time entries for a task"""
    task = Task.query.get_or_404(task_id)
    entries = task.time_entries.order_by(TimeEntry.date.desc()).all()
    return jsonify([e.to_dict() for e in entries]), 200


@tasks_bp.route('/<int:task_id>/time-entries', methods=['POST'])
@jwt_required()
def add_time_entry(task_id):
    """Add a time entry"""
    user_id = get_jwt_identity()
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    if not data.get('hours'):
        return jsonify({'error': 'Hours is required'}), 400

    entry = TimeEntry(
        task_id=task_id,
        user_id=user_id,
        hours=data['hours'],
        description=data.get('description'),
        date=datetime.fromisoformat(data['date']).date() if data.get('date') else datetime.utcnow().date()
    )

    if data.get('start_time'):
        entry.start_time = datetime.fromisoformat(data['start_time'])
    if data.get('end_time'):
        entry.end_time = datetime.fromisoformat(data['end_time'])

    db.session.add(entry)
    db.session.commit()

    return jsonify(entry.to_dict()), 201


# Tags
@tasks_bp.route('/<int:task_id>/tags', methods=['POST'])
@jwt_required()
def add_tag(task_id):
    """Add a tag to a task"""
    task = Task.query.get_or_404(task_id)
    data = request.get_json()

    tag_name = data.get('name') or data.get('tag')
    if not tag_name:
        return jsonify({'error': 'Tag name is required'}), 400

    # Get or create tag
    tag = Tag.query.filter_by(name=tag_name).first()
    if not tag:
        tag = Tag(name=tag_name, color=data.get('color', '#6B7280'))
        db.session.add(tag)
        db.session.flush()

    # Check if already tagged
    existing = TaskTag.query.filter_by(task_id=task_id, tag_id=tag.id).first()
    if existing:
        return jsonify({'message': 'Tag already exists'}), 200

    task_tag = TaskTag(task_id=task_id, tag_id=tag.id)
    db.session.add(task_tag)
    db.session.commit()

    return jsonify(tag.to_dict()), 201


@tasks_bp.route('/<int:task_id>/tags/<int:tag_id>', methods=['DELETE'])
@jwt_required()
def remove_tag(task_id, tag_id):
    """Remove a tag from a task"""
    task_tag = TaskTag.query.filter_by(task_id=task_id, tag_id=tag_id).first_or_404()
    db.session.delete(task_tag)
    db.session.commit()
    return jsonify({'message': 'Tag removed'}), 200


# Tags list
@tasks_bp.route('/tags', methods=['GET'])
@jwt_required()
def get_all_tags():
    """Get all tags"""
    tags = Tag.query.all()
    return jsonify([t.to_dict() for t in tags]), 200
