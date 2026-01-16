"""
Projects API endpoints
"""
from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Project, ProjectBaseline, Milestone, Board

projects_bp = Blueprint('projects', __name__)


@projects_bp.route('', methods=['GET'])
@jwt_required()
def get_projects():
    """Get all projects"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    program_id = request.args.get('program_id', type=int)
    status = request.args.get('status')
    owner_id = request.args.get('owner_id', type=int)
    search = request.args.get('search')

    query = Project.query

    if program_id:
        query = query.filter_by(program_id=program_id)
    if status:
        query = query.filter_by(status=status)
    if owner_id:
        query = query.filter_by(owner_id=owner_id)
    if search:
        query = query.filter(
            db.or_(
                Project.name.ilike(f'%{search}%'),
                Project.code.ilike(f'%{search}%')
            )
        )

    pagination = query.order_by(Project.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'projects': [p.to_dict() for p in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@projects_bp.route('', methods=['POST'])
@jwt_required()
def create_project():
    """Create a new project"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Project name is required'}), 400

    # Generate project code if not provided
    code = data.get('code')
    if not code:
        count = Project.query.count() + 1
        code = f"PRJ-{count:04d}"

    project = Project(
        name=data['name'],
        description=data.get('description'),
        code=code,
        program_id=data.get('program_id'),
        owner_id=data.get('owner_id', user_id),
        template_id=data.get('template_id'),
        status=data.get('status', 'planning'),
        priority=data.get('priority', 'medium'),
        budget=data.get('budget', 0.0),
        currency=data.get('currency', 'USD')
    )

    if data.get('start_date'):
        project.start_date = datetime.fromisoformat(data['start_date']).date()
    if data.get('target_end_date'):
        project.target_end_date = datetime.fromisoformat(data['target_end_date']).date()

    db.session.add(project)
    db.session.flush()

    # Create default board
    board = Board(
        project_id=project.id,
        name='Main Board',
        view_type='kanban',
        is_default=True
    )
    db.session.add(board)
    db.session.flush()
    board.create_default_columns()

    # Apply template if provided
    if data.get('template_id'):
        from app.models import Template
        template = Template.query.get(data['template_id'])
        if template:
            template.apply_to_project(project)

    db.session.commit()
    return jsonify(project.to_dict(include_boards=True)), 201


@projects_bp.route('/<int:project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    """Get a specific project"""
    project = Project.query.get_or_404(project_id)
    include_boards = request.args.get('include_boards', 'false').lower() == 'true'
    include_milestones = request.args.get('include_milestones', 'false').lower() == 'true'
    return jsonify(project.to_dict(include_boards=include_boards, include_milestones=include_milestones)), 200


@projects_bp.route('/<int:project_id>', methods=['PUT'])
@jwt_required()
def update_project(project_id):
    """Update a project"""
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    allowed_fields = ['name', 'description', 'program_id', 'owner_id',
                      'status', 'priority', 'health', 'budget', 'actual_cost',
                      'currency', 'settings']

    for field in allowed_fields:
        if field in data:
            setattr(project, field, data[field])

    # Handle date fields
    if 'start_date' in data:
        project.start_date = datetime.fromisoformat(data['start_date']).date() if data['start_date'] else None
    if 'target_end_date' in data:
        project.target_end_date = datetime.fromisoformat(data['target_end_date']).date() if data['target_end_date'] else None
    if 'actual_end_date' in data:
        project.actual_end_date = datetime.fromisoformat(data['actual_end_date']).date() if data['actual_end_date'] else None

    db.session.commit()
    return jsonify(project.to_dict()), 200


@projects_bp.route('/<int:project_id>', methods=['DELETE'])
@jwt_required()
def delete_project(project_id):
    """Delete a project"""
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted'}), 200


# Baseline endpoints
@projects_bp.route('/<int:project_id>/baselines', methods=['GET'])
@jwt_required()
def get_baselines(project_id):
    """Get project baselines"""
    project = Project.query.get_or_404(project_id)
    baselines = project.baselines.order_by(ProjectBaseline.created_at.desc()).all()
    return jsonify([b.to_dict() for b in baselines]), 200


@projects_bp.route('/<int:project_id>/baselines', methods=['POST'])
@jwt_required()
def create_baseline(project_id):
    """Create a new baseline"""
    user_id = get_jwt_identity()
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    baseline = project.create_baseline(name=data.get('name'))
    baseline.description = data.get('description')
    baseline.created_by_id = user_id

    db.session.commit()
    return jsonify(baseline.to_dict()), 201


@projects_bp.route('/<int:project_id>/baselines/<int:baseline_id>/compare', methods=['GET'])
@jwt_required()
def compare_baseline(project_id, baseline_id):
    """Compare baseline with current state"""
    baseline = ProjectBaseline.query.filter_by(
        id=baseline_id, project_id=project_id
    ).first_or_404()

    comparison = baseline.compare_with_current()
    return jsonify({
        'baseline': baseline.to_dict(),
        'comparison': comparison
    }), 200


# Milestone endpoints
@projects_bp.route('/<int:project_id>/milestones', methods=['GET'])
@jwt_required()
def get_milestones(project_id):
    """Get project milestones"""
    project = Project.query.get_or_404(project_id)
    milestones = project.milestones.order_by(Milestone.due_date).all()
    return jsonify([m.to_dict() for m in milestones]), 200


@projects_bp.route('/<int:project_id>/milestones', methods=['POST'])
@jwt_required()
def create_milestone(project_id):
    """Create a milestone"""
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Milestone name is required'}), 400

    milestone = Milestone(
        project_id=project_id,
        name=data['name'],
        description=data.get('description'),
        color=data.get('color', '#F59E0B')
    )

    if data.get('due_date'):
        milestone.due_date = datetime.fromisoformat(data['due_date']).date()

    db.session.add(milestone)
    db.session.commit()
    return jsonify(milestone.to_dict()), 201


@projects_bp.route('/milestones/<int:milestone_id>', methods=['PUT'])
@jwt_required()
def update_milestone(milestone_id):
    """Update a milestone"""
    milestone = Milestone.query.get_or_404(milestone_id)
    data = request.get_json()

    allowed_fields = ['name', 'description', 'status', 'color']
    for field in allowed_fields:
        if field in data:
            setattr(milestone, field, data[field])

    if 'due_date' in data:
        milestone.due_date = datetime.fromisoformat(data['due_date']).date() if data['due_date'] else None
    if 'completed_date' in data:
        milestone.completed_date = datetime.fromisoformat(data['completed_date']).date() if data['completed_date'] else None

    db.session.commit()
    return jsonify(milestone.to_dict()), 200


# Critical path endpoint
@projects_bp.route('/<int:project_id>/critical-path', methods=['GET'])
@jwt_required()
def get_critical_path(project_id):
    """Calculate and return critical path"""
    from app.services.critical_path import CriticalPathCalculator

    project = Project.query.get_or_404(project_id)
    calculator = CriticalPathCalculator(project)
    result = calculator.calculate()

    return jsonify(result), 200


# Gantt data endpoint
@projects_bp.route('/<int:project_id>/gantt', methods=['GET'])
@jwt_required()
def get_gantt_data(project_id):
    """Get data formatted for Gantt chart"""
    project = Project.query.get_or_404(project_id)

    tasks_data = []
    for board in project.boards:
        for task in board.tasks:
            tasks_data.append({
                'id': task.id,
                'title': task.title,
                'start': task.start_date.isoformat() if task.start_date else None,
                'end': task.due_date.isoformat() if task.due_date else None,
                'progress': task.progress,
                'status': task.status,
                'assignee': task.assignee.name if task.assignee else None,
                'dependencies': [d.depends_on_id for d in task.dependencies],
                'parent_id': task.parent_id
            })

    milestones_data = [{
        'id': f"m-{m.id}",
        'title': m.name,
        'date': m.due_date.isoformat() if m.due_date else None,
        'status': m.status,
        'type': 'milestone'
    } for m in project.milestones]

    return jsonify({
        'project': {
            'id': project.id,
            'name': project.name,
            'start_date': project.start_date.isoformat() if project.start_date else None,
            'end_date': project.target_end_date.isoformat() if project.target_end_date else None
        },
        'tasks': tasks_data,
        'milestones': milestones_data
    }), 200
