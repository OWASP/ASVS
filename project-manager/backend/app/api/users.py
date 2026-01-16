"""
Users API endpoints
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import User, Team, TeamMember, Skill, UserSkill

users_bp = Blueprint('users', __name__)


@users_bp.route('', methods=['GET'])
@jwt_required()
def get_users():
    """Get all users with optional filtering"""
    # Query parameters
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    search = request.args.get('search', '')
    role = request.args.get('role')
    team_id = request.args.get('team_id', type=int)
    skill = request.args.get('skill')

    query = User.query.filter_by(is_active=True)

    # Apply filters
    if search:
        query = query.filter(
            db.or_(
                User.name.ilike(f'%{search}%'),
                User.email.ilike(f'%{search}%')
            )
        )
    if role:
        query = query.filter_by(role=role)
    if team_id:
        query = query.join(TeamMember).filter(TeamMember.team_id == team_id)
    if skill:
        query = query.join(UserSkill).join(Skill).filter(Skill.name.ilike(f'%{skill}%'))

    # Paginate
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        'users': [u.to_dict() for u in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@users_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """Get a specific user"""
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200


@users_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    """Update a user (admin only)"""
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    if current_user.role != 'admin' and current_user_id != user_id:
        return jsonify({'error': 'Not authorized'}), 403

    user = User.query.get_or_404(user_id)
    data = request.get_json()

    # Update fields
    allowed_fields = ['name', 'avatar_url', 'role', 'is_active',
                      'weekly_capacity_hours', 'working_hours_start',
                      'working_hours_end', 'timezone']

    # Only admin can change role
    if 'role' in data and current_user.role != 'admin':
        del data['role']

    for field in allowed_fields:
        if field in data:
            setattr(user, field, data[field])

    db.session.commit()
    return jsonify(user.to_dict()), 200


@users_bp.route('/<int:user_id>/workload', methods=['GET'])
@jwt_required()
def get_user_workload(user_id):
    """Get user's workload and capacity"""
    from datetime import datetime, timedelta
    from app.models import Task, TimeEntry

    user = User.query.get_or_404(user_id)

    # Get date range
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date:
        start_date = datetime.fromisoformat(start_date).date()
    else:
        start_date = datetime.utcnow().date()

    if end_date:
        end_date = datetime.fromisoformat(end_date).date()
    else:
        end_date = start_date + timedelta(days=30)

    # Get assigned tasks
    tasks = Task.query.filter(
        Task.assignee_id == user_id,
        Task.status.notin_(['completed', 'cancelled']),
        db.or_(
            Task.due_date.between(start_date, end_date),
            Task.start_date.between(start_date, end_date)
        )
    ).all()

    # Calculate workload
    total_estimated_hours = sum(t.estimated_hours or 0 for t in tasks)

    # Get time entries for the period
    time_entries = TimeEntry.query.filter(
        TimeEntry.user_id == user_id,
        TimeEntry.date.between(start_date, end_date)
    ).all()

    total_logged_hours = sum(te.hours for te in time_entries)

    # Calculate capacity
    days = (end_date - start_date).days + 1
    weeks = days / 7
    total_capacity = user.weekly_capacity_hours * weeks

    # Utilization
    utilization = (total_estimated_hours / total_capacity * 100) if total_capacity > 0 else 0

    return jsonify({
        'user_id': user_id,
        'start_date': start_date.isoformat(),
        'end_date': end_date.isoformat(),
        'assigned_tasks': len(tasks),
        'total_estimated_hours': total_estimated_hours,
        'total_logged_hours': total_logged_hours,
        'total_capacity_hours': total_capacity,
        'utilization_percentage': round(utilization, 1),
        'status': 'overallocated' if utilization > 100 else 'underutilized' if utilization < 70 else 'optimal',
        'tasks': [t.to_dict(include_dependencies=False) for t in tasks]
    }), 200


@users_bp.route('/<int:user_id>/skills', methods=['GET'])
@jwt_required()
def get_user_skills(user_id):
    """Get user's skills"""
    user = User.query.get_or_404(user_id)
    skills = [{
        'skill': us.skill.to_dict(),
        'proficiency': us.proficiency
    } for us in user.skills]
    return jsonify(skills), 200


@users_bp.route('/<int:user_id>/skills', methods=['POST'])
@jwt_required()
def add_user_skill(user_id):
    """Add a skill to user"""
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    skill_id = data.get('skill_id')
    skill_name = data.get('skill_name')
    proficiency = data.get('proficiency', 3)

    # Get or create skill
    if skill_id:
        skill = Skill.query.get_or_404(skill_id)
    elif skill_name:
        skill = Skill.query.filter_by(name=skill_name).first()
        if not skill:
            skill = Skill(name=skill_name, category=data.get('category', 'technical'))
            db.session.add(skill)
            db.session.flush()
    else:
        return jsonify({'error': 'skill_id or skill_name required'}), 400

    # Check if already has skill
    existing = UserSkill.query.filter_by(user_id=user_id, skill_id=skill.id).first()
    if existing:
        existing.proficiency = proficiency
    else:
        user_skill = UserSkill(user_id=user_id, skill_id=skill.id, proficiency=proficiency)
        db.session.add(user_skill)

    db.session.commit()
    return jsonify({'message': 'Skill added', 'skill': skill.to_dict()}), 201


# Teams endpoints
@users_bp.route('/teams', methods=['GET'])
@jwt_required()
def get_teams():
    """Get all teams"""
    teams = Team.query.all()
    return jsonify([t.to_dict() for t in teams]), 200


@users_bp.route('/teams', methods=['POST'])
@jwt_required()
def create_team():
    """Create a new team"""
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Team name is required'}), 400

    team = Team(
        name=data['name'],
        description=data.get('description'),
        color=data.get('color', '#3B82F6'),
        default_capacity_hours=data.get('default_capacity_hours', 40.0)
    )
    db.session.add(team)
    db.session.commit()

    return jsonify(team.to_dict()), 201


@users_bp.route('/teams/<int:team_id>/members', methods=['POST'])
@jwt_required()
def add_team_member(team_id):
    """Add a member to a team"""
    team = Team.query.get_or_404(team_id)
    data = request.get_json()

    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    user = User.query.get_or_404(user_id)

    # Check if already a member
    existing = TeamMember.query.filter_by(team_id=team_id, user_id=user_id).first()
    if existing:
        return jsonify({'error': 'User is already a team member'}), 409

    member = TeamMember(
        team_id=team_id,
        user_id=user_id,
        role=data.get('role', 'member')
    )
    db.session.add(member)
    db.session.commit()

    return jsonify({'message': 'Member added', 'team': team.to_dict()}), 201


# Skills endpoints
@users_bp.route('/skills', methods=['GET'])
@jwt_required()
def get_skills():
    """Get all skills"""
    category = request.args.get('category')
    query = Skill.query
    if category:
        query = query.filter_by(category=category)
    skills = query.all()
    return jsonify([s.to_dict() for s in skills]), 200


@users_bp.route('/skills', methods=['POST'])
@jwt_required()
def create_skill():
    """Create a new skill"""
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Skill name is required'}), 400

    existing = Skill.query.filter_by(name=data['name']).first()
    if existing:
        return jsonify({'error': 'Skill already exists'}), 409

    skill = Skill(
        name=data['name'],
        category=data.get('category', 'technical'),
        description=data.get('description')
    )
    db.session.add(skill)
    db.session.commit()

    return jsonify(skill.to_dict()), 201
