"""
Notification Model
"""
from datetime import datetime
from app import db


class Notification(db.Model):
    """User notifications"""
    __tablename__ = 'notifications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Notification content
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text)
    notification_type = db.Column(db.String(50))
    # task_assigned, task_due, comment_mention, risk_escalation,
    # project_update, automation_triggered, milestone_due

    # Related entity
    entity_type = db.Column(db.String(30))  # task, project, risk, comment, etc.
    entity_id = db.Column(db.Integer)

    # State
    is_read = db.Column(db.Boolean, default=False)
    read_at = db.Column(db.DateTime)

    # Priority
    priority = db.Column(db.String(10), default='normal')  # low, normal, high, urgent

    # Action URL (for frontend navigation)
    action_url = db.Column(db.String(255))

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    user = db.relationship('User', back_populates='notifications')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'message': self.message,
            'notification_type': self.notification_type,
            'entity_type': self.entity_type,
            'entity_id': self.entity_id,
            'is_read': self.is_read,
            'read_at': self.read_at.isoformat() if self.read_at else None,
            'priority': self.priority,
            'action_url': self.action_url,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def mark_as_read(self):
        """Mark notification as read"""
        self.is_read = True
        self.read_at = datetime.utcnow()

    @staticmethod
    def create_notification(user_id, title, message=None, notification_type=None,
                           entity_type=None, entity_id=None, priority='normal',
                           action_url=None):
        """Helper to create a notification"""
        notification = Notification(
            user_id=user_id,
            title=title,
            message=message,
            notification_type=notification_type,
            entity_type=entity_type,
            entity_id=entity_id,
            priority=priority,
            action_url=action_url
        )
        db.session.add(notification)
        return notification

    def __repr__(self):
        return f'<Notification {self.title[:30]}>'
