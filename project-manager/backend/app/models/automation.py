"""
Automation Models - Workflow automation rules and actions
"""
from datetime import datetime
from app import db


class Automation(db.Model):
    """Automation rules for trigger-based workflows"""
    __tablename__ = 'automations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    # Scope - can be global, portfolio, program, or project level
    scope_type = db.Column(db.String(20), default='project')  # global, portfolio, program, project
    scope_id = db.Column(db.Integer)  # ID of the scoped entity

    # Trigger configuration
    trigger_type = db.Column(db.String(50), nullable=False)
    # task_created, task_updated, task_status_changed, task_assigned,
    # due_date_approaching, due_date_passed, comment_added,
    # risk_status_changed, milestone_due, custom_field_changed

    trigger_conditions = db.Column(db.JSON, default=dict)
    # Conditions that must be met for trigger to fire
    # Example: {"status": "completed", "priority": "high"}

    # State
    is_active = db.Column(db.Boolean, default=True)
    run_count = db.Column(db.Integer, default=0)
    last_run = db.Column(db.DateTime)

    # Creator
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    created_by = db.relationship('User', backref='created_automations')
    actions = db.relationship('AutomationAction', back_populates='automation',
                             lazy='dynamic', cascade='all, delete-orphan',
                             order_by='AutomationAction.order')
    logs = db.relationship('AutomationLog', back_populates='automation',
                          lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self, include_actions=True):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'scope_type': self.scope_type,
            'scope_id': self.scope_id,
            'trigger_type': self.trigger_type,
            'trigger_conditions': self.trigger_conditions,
            'is_active': self.is_active,
            'run_count': self.run_count,
            'last_run': self.last_run.isoformat() if self.last_run else None,
            'created_by_id': self.created_by_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        if include_actions:
            data['actions'] = [a.to_dict() for a in self.actions]
        return data

    def check_conditions(self, entity, changes=None):
        """Check if trigger conditions are met"""
        if not self.trigger_conditions:
            return True

        for field, expected_value in self.trigger_conditions.items():
            actual_value = getattr(entity, field, None)

            # Handle "any" value
            if expected_value == '*':
                continue

            # Handle list of acceptable values
            if isinstance(expected_value, list):
                if actual_value not in expected_value:
                    return False
            # Handle exact match
            elif actual_value != expected_value:
                return False

        return True

    def execute(self, context):
        """Execute all actions in order"""
        from app.services.automation_engine import AutomationEngine
        engine = AutomationEngine()

        results = []
        for action in self.actions.order_by(AutomationAction.order):
            try:
                result = engine.execute_action(action, context)
                results.append({'action_id': action.id, 'success': True, 'result': result})
            except Exception as e:
                results.append({'action_id': action.id, 'success': False, 'error': str(e)})
                if action.stop_on_error:
                    break

        # Update run statistics
        self.run_count += 1
        self.last_run = datetime.utcnow()

        # Log execution
        log = AutomationLog(
            automation_id=self.id,
            trigger_data=context,
            results=results,
            success=all(r['success'] for r in results)
        )
        db.session.add(log)

        return results

    def __repr__(self):
        return f'<Automation {self.name}>'


class AutomationAction(db.Model):
    """Actions to execute when automation triggers"""
    __tablename__ = 'automation_actions'

    id = db.Column(db.Integer, primary_key=True)
    automation_id = db.Column(db.Integer, db.ForeignKey('automations.id'), nullable=False)

    # Action configuration
    action_type = db.Column(db.String(50), nullable=False)
    # update_field, move_to_board, assign_user, send_notification,
    # create_task, add_comment, update_status, send_email,
    # webhook, create_risk, link_dependency

    action_config = db.Column(db.JSON, default=dict)
    # Configuration specific to action type
    # Example for update_field: {"field": "status", "value": "completed"}
    # Example for send_notification: {"type": "email", "template": "task_completed"}

    # Execution order
    order = db.Column(db.Integer, default=0)

    # Error handling
    stop_on_error = db.Column(db.Boolean, default=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    automation = db.relationship('Automation', back_populates='actions')

    def to_dict(self):
        return {
            'id': self.id,
            'automation_id': self.automation_id,
            'action_type': self.action_type,
            'action_config': self.action_config,
            'order': self.order,
            'stop_on_error': self.stop_on_error
        }

    def __repr__(self):
        return f'<AutomationAction {self.action_type}>'


class AutomationLog(db.Model):
    """Log of automation executions"""
    __tablename__ = 'automation_logs'

    id = db.Column(db.Integer, primary_key=True)
    automation_id = db.Column(db.Integer, db.ForeignKey('automations.id'), nullable=False)

    # Execution details
    trigger_data = db.Column(db.JSON)  # Context that triggered the automation
    results = db.Column(db.JSON)  # Results of each action
    success = db.Column(db.Boolean, default=True)
    error_message = db.Column(db.Text)

    executed_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    automation = db.relationship('Automation', back_populates='logs')

    def to_dict(self):
        return {
            'id': self.id,
            'automation_id': self.automation_id,
            'trigger_data': self.trigger_data,
            'results': self.results,
            'success': self.success,
            'error_message': self.error_message,
            'executed_at': self.executed_at.isoformat() if self.executed_at else None
        }

    def __repr__(self):
        return f'<AutomationLog {self.id}>'
