"""
Automation Engine - Executes automation rules based on triggers
"""
from datetime import datetime
from app import db


class AutomationEngine:
    """
    Engine for executing automation rules based on triggers.
    Supports various trigger types and action types.
    """

    def __init__(self):
        self.action_handlers = {
            'update_field': self._action_update_field,
            'assign_user': self._action_assign_user,
            'send_notification': self._action_send_notification,
            'create_task': self._action_create_task,
            'add_comment': self._action_add_comment,
            'update_status': self._action_update_status,
            'move_to_board': self._action_move_to_board,
            'create_risk': self._action_create_risk,
            'webhook': self._action_webhook,
        }

    def trigger(self, trigger_type, entity, changes=None, context=None):
        """
        Trigger automations based on event type.

        Args:
            trigger_type: Type of trigger (task_created, task_status_changed, etc.)
            entity: The entity that triggered the event
            changes: Dict of changes that occurred
            context: Additional context data
        """
        from app.models import Automation

        # Find applicable automations
        automations = Automation.query.filter_by(
            trigger_type=trigger_type,
            is_active=True
        ).all()

        # Filter by scope
        applicable = []
        for automation in automations:
            if self._check_scope(automation, entity):
                if automation.check_conditions(entity, changes):
                    applicable.append(automation)

        # Execute automations
        for automation in applicable:
            try:
                execution_context = {
                    'entity': entity,
                    'changes': changes or {},
                    'context': context or {},
                    'trigger_type': trigger_type
                }
                automation.execute(execution_context)
            except Exception as e:
                # Log error but don't stop other automations
                print(f"Automation {automation.id} failed: {str(e)}")

    def _check_scope(self, automation, entity):
        """Check if automation scope matches the entity"""
        if automation.scope_type == 'global':
            return True

        if automation.scope_type == 'project':
            # Get project ID from entity
            project_id = self._get_project_id(entity)
            return project_id == automation.scope_id

        if automation.scope_type == 'program':
            project_id = self._get_project_id(entity)
            if project_id:
                from app.models import Project
                project = Project.query.get(project_id)
                return project and project.program_id == automation.scope_id

        if automation.scope_type == 'portfolio':
            project_id = self._get_project_id(entity)
            if project_id:
                from app.models import Project
                project = Project.query.get(project_id)
                if project and project.program:
                    return project.program.portfolio_id == automation.scope_id

        return False

    def _get_project_id(self, entity):
        """Get project ID from various entity types"""
        if hasattr(entity, 'project_id'):
            return entity.project_id
        if hasattr(entity, 'board'):
            return entity.board.project_id
        if hasattr(entity, 'board_id'):
            from app.models import Board
            board = Board.query.get(entity.board_id)
            return board.project_id if board else None
        return None

    def execute_action(self, action, context):
        """Execute a single automation action"""
        handler = self.action_handlers.get(action.action_type)
        if not handler:
            raise ValueError(f"Unknown action type: {action.action_type}")

        return handler(action.action_config, context)

    # Action handlers
    def _action_update_field(self, config, context):
        """Update a field on the entity"""
        entity = context['entity']
        field = config.get('field')
        value = config.get('value')

        if hasattr(entity, field):
            setattr(entity, field, value)
            db.session.commit()
            return {'field': field, 'new_value': value}

        return {'error': f'Field {field} not found'}

    def _action_assign_user(self, config, context):
        """Assign a user to the entity"""
        entity = context['entity']
        user_type = config.get('user_type')
        user_id = config.get('user_id')

        if user_type == 'project_owner':
            project_id = self._get_project_id(entity)
            if project_id:
                from app.models import Project
                project = Project.query.get(project_id)
                if project:
                    user_id = project.owner_id

        if user_id and hasattr(entity, 'assignee_id'):
            entity.assignee_id = user_id
            db.session.commit()
            return {'assigned_to': user_id}

        return {'error': 'Could not assign user'}

    def _action_send_notification(self, config, context):
        """Send a notification"""
        from app.models import Notification, User

        entity = context['entity']
        to = config.get('to')
        template = config.get('template')
        priority = config.get('priority', 'normal')

        # Determine recipient
        user_id = None
        if to == 'task_assignee' and hasattr(entity, 'assignee_id'):
            user_id = entity.assignee_id
        elif to == 'task_reporter' and hasattr(entity, 'reporter_id'):
            user_id = entity.reporter_id
        elif to == 'project_owner':
            project_id = self._get_project_id(entity)
            if project_id:
                from app.models import Project
                project = Project.query.get(project_id)
                if project:
                    user_id = project.owner_id
        elif isinstance(to, int):
            user_id = to

        if not user_id:
            return {'error': 'No recipient found'}

        # Create notification
        title = self._get_notification_title(template, entity)
        message = self._get_notification_message(template, entity)

        notification = Notification.create_notification(
            user_id=user_id,
            title=title,
            message=message,
            notification_type=template,
            entity_type=entity.__class__.__name__.lower(),
            entity_id=entity.id,
            priority=priority
        )
        db.session.commit()

        # Emit websocket event
        self._emit_notification(user_id, notification)

        return {'notification_id': notification.id}

    def _action_create_task(self, config, context):
        """Create a new task"""
        from app.models import Task

        entity = context['entity']
        board_id = config.get('board_id')

        if not board_id and hasattr(entity, 'board_id'):
            board_id = entity.board_id

        if not board_id:
            return {'error': 'No board_id specified'}

        task = Task(
            board_id=board_id,
            title=config.get('title', 'Auto-created task'),
            description=config.get('description'),
            status=config.get('status', 'todo'),
            priority=config.get('priority', 'medium')
        )
        db.session.add(task)
        db.session.commit()

        return {'task_id': task.id}

    def _action_add_comment(self, config, context):
        """Add a comment to the entity"""
        from app.models import Comment

        entity = context['entity']

        if not hasattr(entity, 'id') or entity.__class__.__name__ != 'Task':
            return {'error': 'Comments can only be added to tasks'}

        comment = Comment(
            task_id=entity.id,
            author_id=config.get('author_id', 1),  # System user
            content=config.get('content', 'Automated comment')
        )
        db.session.add(comment)
        db.session.commit()

        return {'comment_id': comment.id}

    def _action_update_status(self, config, context):
        """Update status of the entity"""
        entity = context['entity']
        new_status = config.get('status')

        if hasattr(entity, 'status'):
            entity.status = new_status
            db.session.commit()
            return {'new_status': new_status}

        return {'error': 'Entity has no status field'}

    def _action_move_to_board(self, config, context):
        """Move task to a different board"""
        entity = context['entity']
        board_id = config.get('board_id')

        if hasattr(entity, 'board_id'):
            entity.board_id = board_id
            db.session.commit()
            return {'new_board_id': board_id}

        return {'error': 'Entity cannot be moved to board'}

    def _action_create_risk(self, config, context):
        """Create a risk from an issue or task"""
        from app.models import Risk

        entity = context['entity']
        project_id = self._get_project_id(entity)

        if not project_id:
            return {'error': 'Cannot determine project'}

        risk = Risk(
            project_id=project_id,
            title=config.get('title', f'Risk from {entity.__class__.__name__}'),
            description=config.get('description'),
            probability=config.get('probability', 'medium'),
            impact=config.get('impact', 'medium'),
            status='identified'
        )
        risk.calculate_risk_score()
        db.session.add(risk)
        db.session.commit()

        return {'risk_id': risk.id}

    def _action_webhook(self, config, context):
        """Send a webhook to external service"""
        import requests
        import json

        url = config.get('url')
        if not url:
            return {'error': 'No webhook URL specified'}

        entity = context['entity']
        payload = {
            'event': context.get('trigger_type'),
            'entity_type': entity.__class__.__name__,
            'entity_id': entity.id,
            'changes': context.get('changes', {}),
            'timestamp': datetime.utcnow().isoformat()
        }

        # Add custom payload fields
        if config.get('payload'):
            payload.update(config['payload'])

        try:
            response = requests.post(
                url,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=10
            )
            return {
                'status_code': response.status_code,
                'success': response.ok
            }
        except Exception as e:
            return {'error': str(e)}

    def _get_notification_title(self, template, entity):
        """Get notification title based on template"""
        titles = {
            'task_completed': f'Task completed: {getattr(entity, "title", "Unknown")}',
            'task_assigned': f'You have been assigned: {getattr(entity, "title", "Unknown")}',
            'due_date_reminder': f'Due soon: {getattr(entity, "title", "Unknown")}',
            'comment_added': f'New comment on: {getattr(entity, "title", "Unknown")}',
            'high_risk_alert': f'High risk alert: {getattr(entity, "title", "Unknown")}',
            'blocked_task': f'Task blocked: {getattr(entity, "title", "Unknown")}',
        }
        return titles.get(template, 'Notification')

    def _get_notification_message(self, template, entity):
        """Get notification message based on template"""
        messages = {
            'task_completed': 'A task you reported has been marked as completed.',
            'task_assigned': 'You have been assigned a new task.',
            'due_date_reminder': 'This task is due soon. Please review.',
            'comment_added': 'Someone commented on a task you are involved with.',
            'high_risk_alert': 'A risk has been escalated to high priority.',
            'blocked_task': 'A task has been marked as blocked and needs attention.',
        }
        return messages.get(template, '')

    def _emit_notification(self, user_id, notification):
        """Emit notification via WebSocket"""
        try:
            from app import socketio
            socketio.emit(
                'notification',
                notification.to_dict(),
                room=f'user_{user_id}'
            )
        except Exception:
            pass  # WebSocket not available
