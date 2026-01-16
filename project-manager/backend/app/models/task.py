"""
Task Model - Core task entity with dependencies, comments, time tracking
"""
from datetime import datetime
from app import db


class Task(db.Model):
    """Task model - core work item"""
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    # Status and priority
    status = db.Column(db.String(30), default='todo')
    # backlog, todo, in_progress, review, completed, blocked
    priority = db.Column(db.String(10), default='medium')  # low, medium, high, critical
    task_type = db.Column(db.String(20), default='task')  # task, bug, feature, epic, story

    # Assignment
    assignee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    reporter_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Timeline
    start_date = db.Column(db.Date)
    due_date = db.Column(db.Date)
    completed_date = db.Column(db.Date)

    # Time tracking
    estimated_hours = db.Column(db.Float, default=0.0)
    actual_hours = db.Column(db.Float, default=0.0)

    # Progress (0-100)
    progress = db.Column(db.Float, default=0.0)

    # Position for ordering
    position = db.Column(db.Integer, default=0)

    # Parent task for subtasks
    parent_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))

    # Custom fields stored as JSON
    custom_fields = db.Column(db.JSON, default=dict)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    board = db.relationship('Board', back_populates='tasks')
    assignee = db.relationship('User', back_populates='assigned_tasks',
                               foreign_keys=[assignee_id])
    reporter = db.relationship('User', backref='reported_tasks',
                              foreign_keys=[reporter_id])
    parent = db.relationship('Task', remote_side=[id], backref='subtasks')

    comments = db.relationship('Comment', back_populates='task', lazy='dynamic',
                              cascade='all, delete-orphan')
    attachments = db.relationship('Attachment', back_populates='task', lazy='dynamic',
                                 cascade='all, delete-orphan')
    time_entries = db.relationship('TimeEntry', back_populates='task', lazy='dynamic',
                                  cascade='all, delete-orphan')
    tags = db.relationship('TaskTag', back_populates='task', lazy='dynamic',
                          cascade='all, delete-orphan')

    # Dependencies (tasks this task depends on)
    dependencies = db.relationship(
        'TaskDependency',
        foreign_keys='TaskDependency.task_id',
        back_populates='task',
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    # Dependents (tasks that depend on this task)
    dependents = db.relationship(
        'TaskDependency',
        foreign_keys='TaskDependency.depends_on_id',
        back_populates='depends_on',
        lazy='dynamic'
    )

    def to_dict(self, include_comments=False, include_dependencies=True):
        data = {
            'id': self.id,
            'board_id': self.board_id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'task_type': self.task_type,
            'assignee_id': self.assignee_id,
            'assignee': self.assignee.to_dict() if self.assignee else None,
            'reporter_id': self.reporter_id,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed_date': self.completed_date.isoformat() if self.completed_date else None,
            'estimated_hours': self.estimated_hours,
            'actual_hours': self.get_actual_hours(),
            'progress': self.progress,
            'position': self.position,
            'parent_id': self.parent_id,
            'subtask_count': len(self.subtasks) if self.subtasks else 0,
            'comment_count': self.comments.count(),
            'attachment_count': self.attachments.count(),
            'tags': [tt.tag.to_dict() for tt in self.tags],
            'custom_fields': self.custom_fields,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        if include_comments:
            data['comments'] = [c.to_dict() for c in self.comments.order_by(Comment.created_at.desc())]
        if include_dependencies:
            data['dependencies'] = [d.to_dict() for d in self.dependencies]
            data['dependents'] = [d.to_dict() for d in self.dependents]
        return data

    def get_actual_hours(self):
        """Calculate actual hours from time entries"""
        total = 0.0
        for entry in self.time_entries:
            total += entry.hours
        return total

    def is_blocked(self):
        """Check if task is blocked by incomplete dependencies"""
        for dep in self.dependencies:
            if dep.depends_on.status != 'completed':
                return True
        return False

    def can_start(self):
        """Check if all dependencies are met"""
        return not self.is_blocked()

    def __repr__(self):
        return f'<Task {self.title[:30]}>'


class TaskDependency(db.Model):
    """Task dependencies for predecessor/successor relationships"""
    __tablename__ = 'task_dependencies'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    depends_on_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    dependency_type = db.Column(db.String(20), default='finish_to_start')
    # finish_to_start, start_to_start, finish_to_finish, start_to_finish
    lag_days = db.Column(db.Integer, default=0)  # Lag time in days

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    task = db.relationship('Task', foreign_keys=[task_id], back_populates='dependencies')
    depends_on = db.relationship('Task', foreign_keys=[depends_on_id], back_populates='dependents')

    __table_args__ = (
        db.UniqueConstraint('task_id', 'depends_on_id', name='unique_dependency'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'task_id': self.task_id,
            'depends_on_id': self.depends_on_id,
            'depends_on_title': self.depends_on.title if self.depends_on else None,
            'dependency_type': self.dependency_type,
            'lag_days': self.lag_days
        }

    def __repr__(self):
        return f'<TaskDependency {self.task_id} -> {self.depends_on_id}>'


class Comment(db.Model):
    """Task comments for collaboration"""
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('comments.id'))  # For threaded comments

    # Mentions stored as JSON array of user IDs
    mentions = db.Column(db.JSON, default=list)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    task = db.relationship('Task', back_populates='comments')
    author = db.relationship('User', back_populates='comments')
    parent = db.relationship('Comment', remote_side=[id], backref='replies')

    def to_dict(self):
        return {
            'id': self.id,
            'task_id': self.task_id,
            'author_id': self.author_id,
            'author': self.author.to_dict() if self.author else None,
            'content': self.content,
            'parent_id': self.parent_id,
            'mentions': self.mentions,
            'reply_count': len(self.replies) if self.replies else 0,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Comment {self.id}>'


class Attachment(db.Model):
    """File attachments for tasks"""
    __tablename__ = 'attachments'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    filename = db.Column(db.String(255), nullable=False)
    original_filename = db.Column(db.String(255), nullable=False)
    file_path = db.Column(db.String(500), nullable=False)
    file_size = db.Column(db.Integer)  # Size in bytes
    mime_type = db.Column(db.String(100))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    task = db.relationship('Task', back_populates='attachments')
    uploader = db.relationship('User', backref='uploaded_attachments')

    def to_dict(self):
        return {
            'id': self.id,
            'task_id': self.task_id,
            'uploader_id': self.uploader_id,
            'filename': self.filename,
            'original_filename': self.original_filename,
            'file_size': self.file_size,
            'mime_type': self.mime_type,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Attachment {self.original_filename}>'


class TimeEntry(db.Model):
    """Time tracking entries"""
    __tablename__ = 'time_entries'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    hours = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.Date, default=datetime.utcnow().date)

    # For timer-based entries
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    task = db.relationship('Task', back_populates='time_entries')
    user = db.relationship('User', back_populates='time_entries')

    def to_dict(self):
        return {
            'id': self.id,
            'task_id': self.task_id,
            'user_id': self.user_id,
            'user': self.user.to_dict() if self.user else None,
            'hours': self.hours,
            'description': self.description,
            'date': self.date.isoformat() if self.date else None,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<TimeEntry {self.hours}h on {self.date}>'


class Tag(db.Model):
    """Tags for categorizing tasks"""
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    color = db.Column(db.String(7), default='#6B7280')

    # Relationships
    tasks = db.relationship('TaskTag', back_populates='tag', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color
        }

    def __repr__(self):
        return f'<Tag {self.name}>'


class TaskTag(db.Model):
    """Association table for task-tag relationship"""
    __tablename__ = 'task_tags'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)

    # Relationships
    task = db.relationship('Task', back_populates='tags')
    tag = db.relationship('Tag', back_populates='tasks')

    __table_args__ = (
        db.UniqueConstraint('task_id', 'tag_id', name='unique_task_tag'),
    )
