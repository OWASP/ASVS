"""
Resource Allocator - AI-powered resource allocation suggestions
"""
from datetime import datetime, timedelta
from collections import defaultdict


class ResourceAllocator:
    """
    Provides intelligent resource allocation suggestions based on
    workload, skills, and availability.
    """

    def __init__(self):
        pass

    def suggest_assignee(self, task, candidates=None):
        """
        Suggest the best assignee for a task based on various factors.

        Args:
            task: Task to assign
            candidates: List of User objects to consider (optional)

        Returns:
            List of suggested users with scores
        """
        from app.models import User, Task, UserSkill, Skill
        from app import db

        if candidates is None:
            candidates = User.query.filter_by(is_active=True).all()

        if not candidates:
            return []

        suggestions = []
        today = datetime.utcnow().date()
        week_end = today + timedelta(days=7)

        for user in candidates:
            score = 100  # Base score
            factors = []

            # Factor 1: Current workload (0-30 points)
            current_tasks = Task.query.filter(
                Task.assignee_id == user.id,
                Task.status.notin_(['completed', 'cancelled']),
                Task.due_date.between(today, week_end)
            ).count()

            workload_score = max(0, 30 - (current_tasks * 5))
            score += workload_score
            factors.append({
                'factor': 'workload',
                'value': current_tasks,
                'score': workload_score,
                'description': f'{current_tasks} tasks this week'
            })

            # Factor 2: Skill match (0-40 points)
            if task.custom_fields and task.custom_fields.get('required_skills'):
                required_skills = task.custom_fields['required_skills']
                user_skills = [us.skill.name.lower() for us in user.skills]
                matched = sum(1 for skill in required_skills if skill.lower() in user_skills)
                skill_score = (matched / len(required_skills)) * 40 if required_skills else 0
                score += skill_score
                factors.append({
                    'factor': 'skills',
                    'value': matched,
                    'score': skill_score,
                    'description': f'{matched}/{len(required_skills)} skills matched'
                })

            # Factor 3: Capacity (0-20 points)
            estimated_hours = task.estimated_hours or 0
            available_capacity = self._get_available_capacity(user, today, week_end)
            if available_capacity >= estimated_hours:
                capacity_score = 20
            elif available_capacity > 0:
                capacity_score = (available_capacity / estimated_hours) * 20
            else:
                capacity_score = 0
            score += capacity_score
            factors.append({
                'factor': 'capacity',
                'value': available_capacity,
                'score': capacity_score,
                'description': f'{available_capacity:.1f}h available'
            })

            # Factor 4: Recent activity on similar tasks (0-10 points)
            # Prefer users who recently worked on similar task types
            similar_completed = Task.query.filter(
                Task.assignee_id == user.id,
                Task.task_type == task.task_type,
                Task.status == 'completed',
                Task.completed_date >= today - timedelta(days=30)
            ).count()
            activity_score = min(10, similar_completed * 2)
            score += activity_score
            factors.append({
                'factor': 'experience',
                'value': similar_completed,
                'score': activity_score,
                'description': f'{similar_completed} similar tasks completed recently'
            })

            suggestions.append({
                'user': user.to_dict(),
                'score': round(score, 1),
                'factors': factors,
                'recommended': score >= 120
            })

        # Sort by score descending
        suggestions.sort(key=lambda x: x['score'], reverse=True)

        return suggestions

    def _get_available_capacity(self, user, start_date, end_date):
        """Calculate available capacity for a user in a date range"""
        from app.models import Task

        # Total capacity for the period
        days = (end_date - start_date).days + 1
        weeks = days / 7
        total_capacity = user.weekly_capacity_hours * weeks

        # Allocated hours
        allocated = 0
        tasks = Task.query.filter(
            Task.assignee_id == user.id,
            Task.status.notin_(['completed', 'cancelled']),
            Task.due_date.between(start_date, end_date)
        ).all()

        for task in tasks:
            allocated += task.estimated_hours or 0

        return max(0, total_capacity - allocated)

    def balance_workload(self, project_id=None, team_id=None):
        """
        Suggest workload balancing across team members.

        Returns suggestions for task reassignments to balance load.
        """
        from app.models import User, Task, Board, TeamMember
        from app import db

        today = datetime.utcnow().date()
        week_end = today + timedelta(days=14)  # Two weeks

        # Get users
        if team_id:
            user_ids = db.session.query(TeamMember.user_id).filter_by(team_id=team_id).all()
            user_ids = [u[0] for u in user_ids]
            users = User.query.filter(User.id.in_(user_ids), User.is_active == True).all()
        else:
            users = User.query.filter_by(is_active=True).all()

        # Calculate current workload for each user
        workloads = {}
        for user in users:
            tasks_query = Task.query.filter(
                Task.assignee_id == user.id,
                Task.status.notin_(['completed', 'cancelled']),
                Task.due_date.between(today, week_end)
            )

            if project_id:
                tasks_query = tasks_query.join(Board).filter(Board.project_id == project_id)

            tasks = tasks_query.all()
            total_hours = sum(t.estimated_hours or 0 for t in tasks)
            capacity = user.weekly_capacity_hours * 2  # Two weeks

            workloads[user.id] = {
                'user': user,
                'tasks': tasks,
                'total_hours': total_hours,
                'capacity': capacity,
                'utilization': (total_hours / capacity * 100) if capacity > 0 else 0
            }

        # Find overloaded and underutilized users
        overloaded = [w for w in workloads.values() if w['utilization'] > 100]
        underutilized = [w for w in workloads.values() if w['utilization'] < 70]

        suggestions = []

        for over in overloaded:
            excess_hours = over['total_hours'] - over['capacity']

            # Find tasks that could be moved
            moveable_tasks = [
                t for t in over['tasks']
                if t.status == 'todo'  # Only move unstarted tasks
            ]

            for task in moveable_tasks:
                if excess_hours <= 0:
                    break

                # Find best candidate from underutilized
                best_candidate = None
                best_score = 0

                for under in underutilized:
                    available = under['capacity'] - under['total_hours']
                    task_hours = task.estimated_hours or 0

                    if available >= task_hours:
                        # Score based on available capacity
                        score = available - task_hours
                        if score > best_score:
                            best_score = score
                            best_candidate = under

                if best_candidate:
                    suggestions.append({
                        'task': task.to_dict(include_dependencies=False),
                        'from_user': over['user'].to_dict(),
                        'to_user': best_candidate['user'].to_dict(),
                        'reason': f'Rebalance workload: {over["user"].name} is at {over["utilization"]:.0f}% while {best_candidate["user"].name} is at {best_candidate["utilization"]:.0f}%',
                        'hours_moved': task.estimated_hours or 0
                    })

                    # Update tracking
                    excess_hours -= task.estimated_hours or 0
                    best_candidate['total_hours'] += task.estimated_hours or 0
                    best_candidate['utilization'] = (best_candidate['total_hours'] / best_candidate['capacity'] * 100)

        return {
            'suggestions': suggestions,
            'workload_summary': [
                {
                    'user': w['user'].to_dict(),
                    'total_hours': w['total_hours'],
                    'capacity': w['capacity'],
                    'utilization': round(w['utilization'], 1),
                    'status': 'overloaded' if w['utilization'] > 100 else 'underutilized' if w['utilization'] < 70 else 'optimal'
                }
                for w in workloads.values()
            ]
        }

    def predict_bottlenecks(self, project_id, weeks_ahead=4):
        """
        Predict potential resource bottlenecks in upcoming weeks.
        """
        from app.models import Project, Task, Board, User
        from app import db

        project = Project.query.get(project_id)
        if not project:
            return {'error': 'Project not found'}

        today = datetime.utcnow().date()
        predictions = []

        for week in range(weeks_ahead):
            week_start = today + timedelta(weeks=week)
            week_end = week_start + timedelta(days=6)

            # Get tasks due this week
            tasks = Task.query.join(Board).filter(
                Board.project_id == project_id,
                Task.status.notin_(['completed', 'cancelled']),
                Task.due_date.between(week_start, week_end)
            ).all()

            # Group by assignee
            by_assignee = defaultdict(list)
            for task in tasks:
                if task.assignee_id:
                    by_assignee[task.assignee_id].append(task)

            # Check for bottlenecks
            week_bottlenecks = []
            for user_id, user_tasks in by_assignee.items():
                user = User.query.get(user_id)
                if not user:
                    continue

                total_hours = sum(t.estimated_hours or 0 for t in user_tasks)
                capacity = user.weekly_capacity_hours

                if total_hours > capacity:
                    week_bottlenecks.append({
                        'user': user.to_dict(),
                        'allocated_hours': total_hours,
                        'capacity_hours': capacity,
                        'overload_hours': total_hours - capacity,
                        'task_count': len(user_tasks),
                        'severity': 'high' if total_hours > capacity * 1.5 else 'medium'
                    })

            # Check for unassigned tasks
            unassigned = [t for t in tasks if not t.assignee_id]
            unassigned_hours = sum(t.estimated_hours or 0 for t in unassigned)

            predictions.append({
                'week': week + 1,
                'week_start': week_start.isoformat(),
                'week_end': week_end.isoformat(),
                'total_tasks': len(tasks),
                'total_hours': sum(t.estimated_hours or 0 for t in tasks),
                'unassigned_tasks': len(unassigned),
                'unassigned_hours': unassigned_hours,
                'bottlenecks': week_bottlenecks,
                'risk_level': 'high' if week_bottlenecks else 'medium' if unassigned else 'low'
            })

        return {
            'project_id': project_id,
            'predictions': predictions,
            'summary': {
                'weeks_with_bottlenecks': sum(1 for p in predictions if p['bottlenecks']),
                'total_overload_hours': sum(
                    sum(b['overload_hours'] for b in p['bottlenecks'])
                    for p in predictions
                )
            }
        }
