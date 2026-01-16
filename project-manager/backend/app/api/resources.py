"""
Resources API endpoints - Resource planning and allocation
"""
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models import User, Task, TimeEntry, Team, Board

resources_bp = Blueprint('resources', __name__)


@resources_bp.route('/workload', methods=['GET'])
@jwt_required()
def get_workload():
    """Get workload overview for all users or specific team"""
    team_id = request.args.get('team_id', type=int)
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

    # Get users
    if team_id:
        from app.models import TeamMember
        user_ids = db.session.query(TeamMember.user_id).filter_by(team_id=team_id).all()
        user_ids = [u[0] for u in user_ids]
        users = User.query.filter(User.id.in_(user_ids), User.is_active == True).all()
    else:
        users = User.query.filter_by(is_active=True).all()

    workload_data = []
    for user in users:
        # Get assigned tasks in date range
        tasks = Task.query.filter(
            Task.assignee_id == user.id,
            Task.status.notin_(['completed', 'cancelled']),
            db.or_(
                Task.due_date.between(start_date, end_date),
                Task.start_date.between(start_date, end_date),
                db.and_(Task.start_date <= start_date, Task.due_date >= end_date)
            )
        ).all()

        # Calculate totals
        total_estimated = sum(t.estimated_hours or 0 for t in tasks)

        # Calculate capacity for the period
        days = (end_date - start_date).days + 1
        weeks = days / 7
        capacity = user.weekly_capacity_hours * weeks

        # Calculate utilization
        utilization = (total_estimated / capacity * 100) if capacity > 0 else 0

        # Determine status
        if utilization > 100:
            status = 'overallocated'
            color = '#EF4444'  # red
        elif utilization > 80:
            status = 'high'
            color = '#F59E0B'  # yellow
        elif utilization < 50:
            status = 'underutilized'
            color = '#6B7280'  # gray
        else:
            status = 'optimal'
            color = '#10B981'  # green

        workload_data.append({
            'user': user.to_dict(),
            'task_count': len(tasks),
            'estimated_hours': total_estimated,
            'capacity_hours': capacity,
            'utilization_percentage': round(utilization, 1),
            'status': status,
            'color': color,
            'tasks': [{'id': t.id, 'title': t.title, 'due_date': t.due_date.isoformat() if t.due_date else None} for t in tasks[:5]]
        })

    # Sort by utilization (overallocated first)
    workload_data.sort(key=lambda x: x['utilization_percentage'], reverse=True)

    return jsonify({
        'start_date': start_date.isoformat(),
        'end_date': end_date.isoformat(),
        'workload': workload_data,
        'summary': {
            'total_users': len(workload_data),
            'overallocated': sum(1 for w in workload_data if w['status'] == 'overallocated'),
            'optimal': sum(1 for w in workload_data if w['status'] == 'optimal'),
            'underutilized': sum(1 for w in workload_data if w['status'] == 'underutilized')
        }
    }), 200


@resources_bp.route('/forecast', methods=['GET'])
@jwt_required()
def get_forecast():
    """Forecast resource demand based on planned projects"""
    weeks_ahead = request.args.get('weeks', 12, type=int)
    team_id = request.args.get('team_id', type=int)

    today = datetime.utcnow().date()
    forecasts = []

    for week in range(weeks_ahead):
        week_start = today + timedelta(weeks=week)
        week_end = week_start + timedelta(days=6)

        # Get tasks due in this week
        tasks = Task.query.filter(
            Task.status.notin_(['completed', 'cancelled']),
            db.or_(
                Task.due_date.between(week_start, week_end),
                db.and_(Task.start_date <= week_start, Task.due_date >= week_end)
            )
        )

        if team_id:
            from app.models import TeamMember
            user_ids = db.session.query(TeamMember.user_id).filter_by(team_id=team_id).all()
            user_ids = [u[0] for u in user_ids]
            tasks = tasks.filter(Task.assignee_id.in_(user_ids))

        tasks = tasks.all()

        # Calculate demand
        total_demand = sum(t.estimated_hours or 0 for t in tasks)

        # Get capacity
        if team_id:
            users = User.query.filter(User.id.in_(user_ids), User.is_active == True).all()
        else:
            users = User.query.filter_by(is_active=True).all()

        total_capacity = sum(u.weekly_capacity_hours for u in users)

        forecasts.append({
            'week_start': week_start.isoformat(),
            'week_end': week_end.isoformat(),
            'week_number': week + 1,
            'demand_hours': total_demand,
            'capacity_hours': total_capacity,
            'utilization': round((total_demand / total_capacity * 100) if total_capacity > 0 else 0, 1),
            'task_count': len(tasks),
            'gap': total_capacity - total_demand
        })

    return jsonify({
        'forecast': forecasts,
        'weeks': weeks_ahead
    }), 200


@resources_bp.route('/allocate', methods=['POST'])
@jwt_required()
def allocate_resource():
    """Allocate a resource to a task"""
    data = request.get_json()

    if not data.get('task_id') or not data.get('user_id'):
        return jsonify({'error': 'task_id and user_id are required'}), 400

    task = Task.query.get_or_404(data['task_id'])
    user = User.query.get_or_404(data['user_id'])

    task.assignee_id = user.id
    db.session.commit()

    return jsonify({
        'message': 'Resource allocated',
        'task': task.to_dict()
    }), 200


@resources_bp.route('/bulk-allocate', methods=['POST'])
@jwt_required()
def bulk_allocate():
    """Bulk allocate resources"""
    data = request.get_json()

    if not data.get('allocations'):
        return jsonify({'error': 'allocations array is required'}), 400

    results = []
    for allocation in data['allocations']:
        task = Task.query.get(allocation['task_id'])
        if task:
            task.assignee_id = allocation['user_id']
            results.append({'task_id': task.id, 'success': True})
        else:
            results.append({'task_id': allocation['task_id'], 'success': False, 'error': 'Task not found'})

    db.session.commit()
    return jsonify({'results': results}), 200


@resources_bp.route('/skill-match', methods=['GET'])
@jwt_required()
def find_skill_match():
    """Find users with matching skills for a task"""
    skills = request.args.getlist('skills')
    available_only = request.args.get('available_only', 'false').lower() == 'true'

    if not skills:
        return jsonify({'error': 'skills parameter is required'}), 400

    from app.models import Skill, UserSkill

    # Find users with any of the requested skills
    users_query = db.session.query(User, db.func.count(UserSkill.id).label('skill_count'))\
        .join(UserSkill)\
        .join(Skill)\
        .filter(Skill.name.in_(skills), User.is_active == True)\
        .group_by(User.id)\
        .order_by(db.desc('skill_count'))

    users_data = []
    for user, skill_count in users_query.all():
        user_dict = user.to_dict()
        user_dict['matching_skills'] = skill_count

        if available_only:
            # Check current workload
            today = datetime.utcnow().date()
            week_end = today + timedelta(days=7)
            task_count = Task.query.filter(
                Task.assignee_id == user.id,
                Task.status.notin_(['completed', 'cancelled']),
                Task.due_date.between(today, week_end)
            ).count()
            user_dict['current_tasks'] = task_count

            # Skip if heavily loaded
            if task_count > 5:
                continue

        users_data.append(user_dict)

    return jsonify({
        'users': users_data,
        'requested_skills': skills
    }), 200


@resources_bp.route('/capacity-rules', methods=['GET'])
@jwt_required()
def get_capacity_rules():
    """Get capacity rules for users/teams"""
    user_id = request.args.get('user_id', type=int)
    team_id = request.args.get('team_id', type=int)

    if user_id:
        user = User.query.get_or_404(user_id)
        return jsonify({
            'user_id': user.id,
            'weekly_capacity_hours': user.weekly_capacity_hours,
            'working_hours_start': user.working_hours_start,
            'working_hours_end': user.working_hours_end,
            'timezone': user.timezone
        }), 200

    if team_id:
        team = Team.query.get_or_404(team_id)
        return jsonify({
            'team_id': team.id,
            'default_capacity_hours': team.default_capacity_hours,
            'holidays': team.holidays
        }), 200

    return jsonify({'error': 'user_id or team_id required'}), 400


@resources_bp.route('/capacity-rules', methods=['PUT'])
@jwt_required()
def update_capacity_rules():
    """Update capacity rules"""
    data = request.get_json()

    if data.get('user_id'):
        user = User.query.get_or_404(data['user_id'])
        if 'weekly_capacity_hours' in data:
            user.weekly_capacity_hours = data['weekly_capacity_hours']
        if 'working_hours_start' in data:
            user.working_hours_start = data['working_hours_start']
        if 'working_hours_end' in data:
            user.working_hours_end = data['working_hours_end']
        if 'timezone' in data:
            user.timezone = data['timezone']
        db.session.commit()
        return jsonify({'message': 'User capacity updated'}), 200

    if data.get('team_id'):
        team = Team.query.get_or_404(data['team_id'])
        if 'default_capacity_hours' in data:
            team.default_capacity_hours = data['default_capacity_hours']
        if 'holidays' in data:
            team.holidays = data['holidays']
        db.session.commit()
        return jsonify({'message': 'Team capacity updated'}), 200

    return jsonify({'error': 'user_id or team_id required'}), 400


@resources_bp.route('/scenario', methods=['POST'])
@jwt_required()
def scenario_planning():
    """Model resource allocation under different scenarios"""
    data = request.get_json()

    if not data.get('scenario'):
        return jsonify({'error': 'scenario configuration required'}), 400

    scenario = data['scenario']
    results = {
        'scenario_name': scenario.get('name', 'Custom Scenario'),
        'impacts': []
    }

    # Scenario: Add new tasks
    if scenario.get('add_tasks'):
        additional_hours = sum(t.get('hours', 0) for t in scenario['add_tasks'])
        results['impacts'].append({
            'type': 'additional_workload',
            'hours': additional_hours,
            'description': f'Adding {len(scenario["add_tasks"])} new tasks'
        })

    # Scenario: Remove team member
    if scenario.get('remove_user_id'):
        user = User.query.get(scenario['remove_user_id'])
        if user:
            task_count = Task.query.filter(
                Task.assignee_id == user.id,
                Task.status.notin_(['completed', 'cancelled'])
            ).count()
            results['impacts'].append({
                'type': 'capacity_reduction',
                'hours_per_week': user.weekly_capacity_hours,
                'tasks_to_reassign': task_count,
                'description': f'Removing {user.name} from team'
            })

    # Scenario: Change deadline
    if scenario.get('new_deadline'):
        # Calculate compression ratio
        from app.models import Project
        if scenario.get('project_id'):
            project = Project.query.get(scenario['project_id'])
            if project and project.target_end_date:
                new_deadline = datetime.fromisoformat(scenario['new_deadline']).date()
                original_days = (project.target_end_date - datetime.utcnow().date()).days
                new_days = (new_deadline - datetime.utcnow().date()).days
                compression = ((original_days - new_days) / original_days * 100) if original_days > 0 else 0
                results['impacts'].append({
                    'type': 'schedule_compression',
                    'compression_percentage': round(compression, 1),
                    'description': f'Deadline moved from {project.target_end_date} to {new_deadline}'
                })

    return jsonify(results), 200
