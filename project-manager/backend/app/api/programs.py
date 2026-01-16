"""
Programs API endpoints
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Program, OKR, KeyResult

programs_bp = Blueprint('programs', __name__)


@programs_bp.route('', methods=['GET'])
@jwt_required()
def get_programs():
    """Get all programs"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    portfolio_id = request.args.get('portfolio_id', type=int)
    status = request.args.get('status')

    query = Program.query

    if portfolio_id:
        query = query.filter_by(portfolio_id=portfolio_id)
    if status:
        query = query.filter_by(status=status)

    pagination = query.order_by(Program.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'programs': [p.to_dict() for p in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@programs_bp.route('', methods=['POST'])
@jwt_required()
def create_program():
    """Create a new program"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Program name is required'}), 400

    program = Program(
        name=data['name'],
        description=data.get('description'),
        portfolio_id=data.get('portfolio_id'),
        owner_id=data.get('owner_id', user_id),
        status=data.get('status', 'planning'),
        color=data.get('color', '#8B5CF6'),
        budget=data.get('budget', 0.0)
    )

    if data.get('start_date'):
        from datetime import datetime
        program.start_date = datetime.fromisoformat(data['start_date']).date()
    if data.get('target_end_date'):
        program.target_end_date = datetime.fromisoformat(data['target_end_date']).date()

    db.session.add(program)
    db.session.commit()

    return jsonify(program.to_dict()), 201


@programs_bp.route('/<int:program_id>', methods=['GET'])
@jwt_required()
def get_program(program_id):
    """Get a specific program"""
    program = Program.query.get_or_404(program_id)
    include_projects = request.args.get('include_projects', 'false').lower() == 'true'
    include_okrs = request.args.get('include_okrs', 'false').lower() == 'true'
    return jsonify(program.to_dict(include_projects=include_projects, include_okrs=include_okrs)), 200


@programs_bp.route('/<int:program_id>', methods=['PUT'])
@jwt_required()
def update_program(program_id):
    """Update a program"""
    program = Program.query.get_or_404(program_id)
    data = request.get_json()

    allowed_fields = ['name', 'description', 'portfolio_id', 'owner_id',
                      'status', 'color', 'budget', 'actual_cost']

    for field in allowed_fields:
        if field in data:
            setattr(program, field, data[field])

    # Handle date fields
    if 'start_date' in data:
        from datetime import datetime
        program.start_date = datetime.fromisoformat(data['start_date']).date() if data['start_date'] else None
    if 'target_end_date' in data:
        program.target_end_date = datetime.fromisoformat(data['target_end_date']).date() if data['target_end_date'] else None
    if 'actual_end_date' in data:
        program.actual_end_date = datetime.fromisoformat(data['actual_end_date']).date() if data['actual_end_date'] else None

    db.session.commit()
    return jsonify(program.to_dict()), 200


@programs_bp.route('/<int:program_id>', methods=['DELETE'])
@jwt_required()
def delete_program(program_id):
    """Delete a program"""
    program = Program.query.get_or_404(program_id)

    if program.projects.count() > 0:
        return jsonify({'error': 'Cannot delete program with projects'}), 400

    db.session.delete(program)
    db.session.commit()
    return jsonify({'message': 'Program deleted'}), 200


# OKR endpoints
@programs_bp.route('/<int:program_id>/okrs', methods=['GET'])
@jwt_required()
def get_program_okrs(program_id):
    """Get OKRs for a program"""
    program = Program.query.get_or_404(program_id)
    quarter = request.args.get('quarter')
    year = request.args.get('year', type=int)

    query = program.okrs
    if quarter:
        query = query.filter_by(quarter=quarter)
    if year:
        query = query.filter_by(year=year)

    okrs = query.all()
    return jsonify([o.to_dict() for o in okrs]), 200


@programs_bp.route('/<int:program_id>/okrs', methods=['POST'])
@jwt_required()
def create_okr(program_id):
    """Create an OKR for a program"""
    user_id = get_jwt_identity()
    program = Program.query.get_or_404(program_id)
    data = request.get_json()

    if not data.get('objective'):
        return jsonify({'error': 'Objective is required'}), 400

    okr = OKR(
        program_id=program_id,
        objective=data['objective'],
        description=data.get('description'),
        owner_id=data.get('owner_id', user_id),
        quarter=data.get('quarter'),
        year=data.get('year')
    )
    db.session.add(okr)
    db.session.flush()

    # Add key results if provided
    if data.get('key_results'):
        for kr_data in data['key_results']:
            kr = KeyResult(
                okr_id=okr.id,
                description=kr_data['description'],
                metric_type=kr_data.get('metric_type', 'percentage'),
                target_value=kr_data.get('target_value', 100),
                current_value=kr_data.get('current_value', 0),
                unit=kr_data.get('unit')
            )
            db.session.add(kr)

    db.session.commit()
    return jsonify(okr.to_dict()), 201


@programs_bp.route('/okrs/<int:okr_id>', methods=['PUT'])
@jwt_required()
def update_okr(okr_id):
    """Update an OKR"""
    okr = OKR.query.get_or_404(okr_id)
    data = request.get_json()

    allowed_fields = ['objective', 'description', 'owner_id', 'status', 'quarter', 'year']
    for field in allowed_fields:
        if field in data:
            setattr(okr, field, data[field])

    db.session.commit()
    return jsonify(okr.to_dict()), 200


@programs_bp.route('/okrs/<int:okr_id>/key-results', methods=['POST'])
@jwt_required()
def add_key_result(okr_id):
    """Add a key result to an OKR"""
    okr = OKR.query.get_or_404(okr_id)
    data = request.get_json()

    if not data.get('description'):
        return jsonify({'error': 'Description is required'}), 400

    kr = KeyResult(
        okr_id=okr_id,
        description=data['description'],
        metric_type=data.get('metric_type', 'percentage'),
        target_value=data.get('target_value', 100),
        current_value=data.get('current_value', 0),
        unit=data.get('unit')
    )
    db.session.add(kr)
    db.session.commit()

    return jsonify(kr.to_dict()), 201


@programs_bp.route('/key-results/<int:kr_id>', methods=['PUT'])
@jwt_required()
def update_key_result(kr_id):
    """Update a key result"""
    kr = KeyResult.query.get_or_404(kr_id)
    data = request.get_json()

    allowed_fields = ['description', 'metric_type', 'target_value', 'current_value', 'unit']
    for field in allowed_fields:
        if field in data:
            setattr(kr, field, data[field])

    db.session.commit()
    return jsonify(kr.to_dict()), 200


@programs_bp.route('/<int:program_id>/cross-dependencies', methods=['GET'])
@jwt_required()
def get_cross_project_dependencies(program_id):
    """Get cross-project dependencies within a program"""
    from app.models import Task, TaskDependency, Board

    program = Program.query.get_or_404(program_id)

    cross_deps = []
    project_ids = [p.id for p in program.projects]

    # Find tasks that have dependencies on tasks in different projects
    for project in program.projects:
        for board in project.boards:
            for task in board.tasks:
                for dep in task.dependencies:
                    # Get the project of the dependent task
                    dep_task = dep.depends_on
                    dep_board = dep_task.board
                    dep_project = dep_board.project

                    if dep_project.id != project.id and dep_project.id in project_ids:
                        cross_deps.append({
                            'task': task.to_dict(include_dependencies=False),
                            'task_project': {'id': project.id, 'name': project.name},
                            'depends_on': dep_task.to_dict(include_dependencies=False),
                            'depends_on_project': {'id': dep_project.id, 'name': dep_project.name},
                            'dependency_type': dep.dependency_type
                        })

    return jsonify({
        'program_id': program_id,
        'cross_dependencies': cross_deps,
        'count': len(cross_deps)
    }), 200
