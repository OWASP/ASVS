"""
Reports API endpoints
"""
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models import (
    Portfolio, Program, Project, Task, Risk, User,
    TimeEntry, Board
)

reports_bp = Blueprint('reports', __name__)


@reports_bp.route('/portfolio/<int:portfolio_id>', methods=['GET'])
@jwt_required()
def portfolio_report(portfolio_id):
    """Generate portfolio-level report"""
    portfolio = Portfolio.query.get_or_404(portfolio_id)

    programs_data = []
    total_tasks = 0
    completed_tasks = 0
    total_budget = 0
    total_spent = 0
    total_risks = 0
    high_risks = 0

    for program in portfolio.programs:
        program_tasks = 0
        program_completed = 0
        program_risks = Risk.query.join(Project).filter(
            Project.program_id == program.id
        ).count()

        for project in program.projects:
            project_task_count = project.get_task_count()
            project_completed_count = project.get_completed_task_count()

            program_tasks += project_task_count
            program_completed += project_completed_count
            total_budget += project.budget or 0
            total_spent += project.actual_cost or 0

            # Count risks
            project_high_risks = Risk.query.filter(
                Risk.project_id == project.id,
                Risk.risk_score >= 15
            ).count()
            high_risks += project_high_risks

        total_tasks += program_tasks
        completed_tasks += program_completed
        total_risks += program_risks

        programs_data.append({
            'id': program.id,
            'name': program.name,
            'status': program.status,
            'progress': round((program_completed / program_tasks * 100) if program_tasks > 0 else 0, 1),
            'project_count': program.projects.count(),
            'task_count': program_tasks,
            'completed_tasks': program_completed,
            'risk_count': program_risks,
            'budget': program.budget,
            'actual_cost': program.actual_cost
        })

    return jsonify({
        'portfolio': portfolio.to_dict(),
        'summary': {
            'total_programs': portfolio.programs.count(),
            'total_projects': sum(p.projects.count() for p in portfolio.programs),
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'overall_progress': round((completed_tasks / total_tasks * 100) if total_tasks > 0 else 0, 1),
            'total_budget': total_budget,
            'total_spent': total_spent,
            'budget_utilization': round((total_spent / total_budget * 100) if total_budget > 0 else 0, 1),
            'total_risks': total_risks,
            'high_risks': high_risks
        },
        'programs': programs_data
    }), 200


@reports_bp.route('/project/<int:project_id>', methods=['GET'])
@jwt_required()
def project_report(project_id):
    """Generate project-level report"""
    project = Project.query.get_or_404(project_id)

    # Task statistics
    tasks = []
    for board in project.boards:
        tasks.extend(list(board.tasks))

    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t.status == 'completed')
    in_progress_tasks = sum(1 for t in tasks if t.status == 'in_progress')
    blocked_tasks = sum(1 for t in tasks if t.status == 'blocked')
    overdue_tasks = sum(1 for t in tasks if t.due_date and t.due_date < datetime.utcnow().date() and t.status != 'completed')

    # Time tracking
    total_estimated = sum(t.estimated_hours or 0 for t in tasks)
    total_actual = sum(t.get_actual_hours() for t in tasks)

    # Risks
    risks = list(project.risks)
    open_risks = sum(1 for r in risks if r.status not in ['resolved', 'closed'])
    high_risks = sum(1 for r in risks if r.get_risk_level() in ['high', 'critical'])

    # Milestones
    milestones = list(project.milestones)
    completed_milestones = sum(1 for m in milestones if m.status == 'completed')
    overdue_milestones = sum(1 for m in milestones if m.due_date and m.due_date < datetime.utcnow().date() and m.status != 'completed')

    # Team workload
    team_workload = {}
    for task in tasks:
        if task.assignee_id:
            if task.assignee_id not in team_workload:
                team_workload[task.assignee_id] = {
                    'user': task.assignee.to_dict() if task.assignee else None,
                    'total_tasks': 0,
                    'completed_tasks': 0,
                    'estimated_hours': 0
                }
            team_workload[task.assignee_id]['total_tasks'] += 1
            if task.status == 'completed':
                team_workload[task.assignee_id]['completed_tasks'] += 1
            team_workload[task.assignee_id]['estimated_hours'] += task.estimated_hours or 0

    return jsonify({
        'project': project.to_dict(),
        'task_summary': {
            'total': total_tasks,
            'completed': completed_tasks,
            'in_progress': in_progress_tasks,
            'blocked': blocked_tasks,
            'overdue': overdue_tasks,
            'progress': round((completed_tasks / total_tasks * 100) if total_tasks > 0 else 0, 1)
        },
        'time_tracking': {
            'total_estimated_hours': total_estimated,
            'total_actual_hours': total_actual,
            'variance': total_actual - total_estimated,
            'efficiency': round((total_estimated / total_actual * 100) if total_actual > 0 else 100, 1)
        },
        'risk_summary': {
            'total': len(risks),
            'open': open_risks,
            'high_critical': high_risks
        },
        'milestone_summary': {
            'total': len(milestones),
            'completed': completed_milestones,
            'overdue': overdue_milestones
        },
        'team_workload': list(team_workload.values()),
        'budget': {
            'allocated': project.budget,
            'spent': project.actual_cost,
            'remaining': (project.budget or 0) - (project.actual_cost or 0),
            'utilization': round((project.actual_cost / project.budget * 100) if project.budget else 0, 1)
        }
    }), 200


@reports_bp.route('/resource-utilization', methods=['GET'])
@jwt_required()
def resource_utilization_report():
    """Generate resource utilization report"""
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    team_id = request.args.get('team_id', type=int)

    if start_date:
        start_date = datetime.fromisoformat(start_date).date()
    else:
        start_date = datetime.utcnow().date() - timedelta(days=30)

    if end_date:
        end_date = datetime.fromisoformat(end_date).date()
    else:
        end_date = datetime.utcnow().date()

    # Get users
    users_query = User.query.filter_by(is_active=True)
    if team_id:
        from app.models import TeamMember
        user_ids = db.session.query(TeamMember.user_id).filter_by(team_id=team_id).all()
        user_ids = [u[0] for u in user_ids]
        users_query = users_query.filter(User.id.in_(user_ids))

    users = users_query.all()

    utilization_data = []
    for user in users:
        # Get time entries
        time_entries = TimeEntry.query.filter(
            TimeEntry.user_id == user.id,
            TimeEntry.date.between(start_date, end_date)
        ).all()

        logged_hours = sum(te.hours for te in time_entries)

        # Calculate capacity
        days = (end_date - start_date).days + 1
        weeks = days / 7
        capacity = user.weekly_capacity_hours * weeks

        # Get completed tasks
        completed_tasks = Task.query.filter(
            Task.assignee_id == user.id,
            Task.completed_date.between(start_date, end_date)
        ).count()

        utilization_data.append({
            'user': user.to_dict(),
            'logged_hours': logged_hours,
            'capacity_hours': capacity,
            'utilization': round((logged_hours / capacity * 100) if capacity > 0 else 0, 1),
            'completed_tasks': completed_tasks,
            'daily_breakdown': _get_daily_breakdown(user.id, start_date, end_date)
        })

    # Sort by utilization
    utilization_data.sort(key=lambda x: x['utilization'], reverse=True)

    return jsonify({
        'period': {
            'start_date': start_date.isoformat(),
            'end_date': end_date.isoformat()
        },
        'utilization': utilization_data,
        'summary': {
            'total_users': len(utilization_data),
            'average_utilization': round(sum(u['utilization'] for u in utilization_data) / len(utilization_data) if utilization_data else 0, 1),
            'total_logged_hours': sum(u['logged_hours'] for u in utilization_data),
            'total_capacity_hours': sum(u['capacity_hours'] for u in utilization_data)
        }
    }), 200


def _get_daily_breakdown(user_id, start_date, end_date):
    """Get daily hours breakdown for a user"""
    time_entries = TimeEntry.query.filter(
        TimeEntry.user_id == user_id,
        TimeEntry.date.between(start_date, end_date)
    ).all()

    daily = {}
    current = start_date
    while current <= end_date:
        daily[current.isoformat()] = 0
        current += timedelta(days=1)

    for entry in time_entries:
        key = entry.date.isoformat()
        if key in daily:
            daily[key] += entry.hours

    return daily


@reports_bp.route('/risk-summary', methods=['GET'])
@jwt_required()
def risk_summary_report():
    """Generate risk summary report"""
    portfolio_id = request.args.get('portfolio_id', type=int)
    program_id = request.args.get('program_id', type=int)
    project_id = request.args.get('project_id', type=int)

    query = Risk.query

    if project_id:
        query = query.filter_by(project_id=project_id)
    elif program_id:
        query = query.join(Project).filter(Project.program_id == program_id)
    elif portfolio_id:
        query = query.join(Project).join(Program).filter(Program.portfolio_id == portfolio_id)

    risks = query.all()

    # Categorize by status
    status_breakdown = {}
    for risk in risks:
        if risk.status not in status_breakdown:
            status_breakdown[risk.status] = 0
        status_breakdown[risk.status] += 1

    # Categorize by level
    level_breakdown = {'low': 0, 'medium': 0, 'high': 0, 'critical': 0}
    for risk in risks:
        level = risk.get_risk_level()
        level_breakdown[level] += 1

    # Category breakdown
    category_breakdown = {}
    for risk in risks:
        cat = risk.category or 'uncategorized'
        if cat not in category_breakdown:
            category_breakdown[cat] = 0
        category_breakdown[cat] += 1

    # Top risks
    top_risks = sorted(risks, key=lambda r: r.risk_score or 0, reverse=True)[:10]

    # Trend data (risks created per week for last 8 weeks)
    trend_data = []
    for i in range(8):
        week_start = datetime.utcnow().date() - timedelta(weeks=i+1)
        week_end = week_start + timedelta(days=6)
        count = sum(1 for r in risks if r.identified_date and week_start <= r.identified_date <= week_end)
        trend_data.append({
            'week': week_start.isoformat(),
            'new_risks': count
        })
    trend_data.reverse()

    return jsonify({
        'summary': {
            'total_risks': len(risks),
            'open_risks': sum(1 for r in risks if r.status not in ['resolved', 'closed']),
            'high_critical_risks': level_breakdown['high'] + level_breakdown['critical'],
            'average_score': round(sum(r.risk_score or 0 for r in risks) / len(risks) if risks else 0, 1)
        },
        'status_breakdown': status_breakdown,
        'level_breakdown': level_breakdown,
        'category_breakdown': category_breakdown,
        'top_risks': [r.to_dict() for r in top_risks],
        'trend': trend_data
    }), 200


@reports_bp.route('/velocity', methods=['GET'])
@jwt_required()
def velocity_report():
    """Generate velocity/throughput report"""
    project_id = request.args.get('project_id', type=int)
    weeks = request.args.get('weeks', 8, type=int)

    if not project_id:
        return jsonify({'error': 'project_id is required'}), 400

    project = Project.query.get_or_404(project_id)

    velocity_data = []
    for i in range(weeks):
        week_end = datetime.utcnow().date() - timedelta(weeks=i)
        week_start = week_end - timedelta(days=6)

        # Get tasks completed in this week
        completed_tasks = Task.query.join(Board).filter(
            Board.project_id == project_id,
            Task.completed_date.between(week_start, week_end)
        ).all()

        # Calculate story points (using estimated_hours as proxy)
        points_completed = sum(t.estimated_hours or 0 for t in completed_tasks)

        velocity_data.append({
            'week_start': week_start.isoformat(),
            'week_end': week_end.isoformat(),
            'tasks_completed': len(completed_tasks),
            'points_completed': points_completed
        })

    velocity_data.reverse()

    # Calculate averages
    avg_tasks = sum(v['tasks_completed'] for v in velocity_data) / len(velocity_data) if velocity_data else 0
    avg_points = sum(v['points_completed'] for v in velocity_data) / len(velocity_data) if velocity_data else 0

    return jsonify({
        'project_id': project_id,
        'weeks': weeks,
        'velocity': velocity_data,
        'averages': {
            'tasks_per_week': round(avg_tasks, 1),
            'points_per_week': round(avg_points, 1)
        }
    }), 200


@reports_bp.route('/burndown/<int:project_id>', methods=['GET'])
@jwt_required()
def burndown_report(project_id):
    """Generate burndown chart data"""
    project = Project.query.get_or_404(project_id)

    if not project.start_date or not project.target_end_date:
        return jsonify({'error': 'Project must have start and end dates'}), 400

    # Get all tasks
    tasks = []
    for board in project.boards:
        tasks.extend(list(board.tasks))

    total_tasks = len(tasks)
    total_points = sum(t.estimated_hours or 0 for t in tasks)

    # Generate daily burndown data
    burndown = []
    current_date = project.start_date
    end_date = min(project.target_end_date, datetime.utcnow().date())

    while current_date <= end_date:
        # Count remaining tasks as of this date
        remaining_tasks = sum(1 for t in tasks if not t.completed_date or t.completed_date > current_date)
        remaining_points = sum(t.estimated_hours or 0 for t in tasks if not t.completed_date or t.completed_date > current_date)

        burndown.append({
            'date': current_date.isoformat(),
            'remaining_tasks': remaining_tasks,
            'remaining_points': remaining_points
        })
        current_date += timedelta(days=1)

    # Calculate ideal burndown
    project_days = (project.target_end_date - project.start_date).days + 1
    ideal_burndown = []
    for i in range(project_days):
        date = project.start_date + timedelta(days=i)
        ideal_remaining = total_points * (1 - i / (project_days - 1)) if project_days > 1 else 0
        ideal_burndown.append({
            'date': date.isoformat(),
            'ideal_remaining': round(ideal_remaining, 1)
        })

    return jsonify({
        'project_id': project_id,
        'total_tasks': total_tasks,
        'total_points': total_points,
        'actual_burndown': burndown,
        'ideal_burndown': ideal_burndown
    }), 200
