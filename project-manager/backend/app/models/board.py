"""
Board Model - Visual workspace for tasks
"""
from datetime import datetime
from app import db


class Board(db.Model):
    """Board model for visual task management"""
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    view_type = db.Column(db.String(20), default='kanban')  # kanban, table, timeline, calendar
    is_default = db.Column(db.Boolean, default=False)
    position = db.Column(db.Integer, default=0)

    # View settings
    settings = db.Column(db.JSON, default=dict)
    # Includes: filters, grouping, sorting, visible columns, etc.

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    project = db.relationship('Project', back_populates='boards')
    columns = db.relationship('BoardColumn', back_populates='board', lazy='dynamic',
                             cascade='all, delete-orphan', order_by='BoardColumn.position')
    tasks = db.relationship('Task', back_populates='board', lazy='dynamic',
                           cascade='all, delete-orphan')

    def to_dict(self, include_columns=True, include_tasks=False):
        data = {
            'id': self.id,
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'view_type': self.view_type,
            'is_default': self.is_default,
            'position': self.position,
            'settings': self.settings,
            'task_count': self.tasks.count(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        if include_columns:
            data['columns'] = [c.to_dict() for c in self.columns.order_by(BoardColumn.position)]
        if include_tasks:
            data['tasks'] = [t.to_dict() for t in self.tasks]
        return data

    def create_default_columns(self):
        """Create default Kanban columns"""
        default_columns = [
            {'name': 'Backlog', 'status': 'backlog', 'color': '#6B7280'},
            {'name': 'To Do', 'status': 'todo', 'color': '#3B82F6'},
            {'name': 'In Progress', 'status': 'in_progress', 'color': '#F59E0B'},
            {'name': 'Review', 'status': 'review', 'color': '#8B5CF6'},
            {'name': 'Done', 'status': 'completed', 'color': '#10B981'}
        ]
        for i, col_data in enumerate(default_columns):
            column = BoardColumn(
                board_id=self.id,
                name=col_data['name'],
                status_mapping=col_data['status'],
                color=col_data['color'],
                position=i
            )
            db.session.add(column)

    def __repr__(self):
        return f'<Board {self.name}>'


class BoardColumn(db.Model):
    """Board columns for Kanban-style organization"""
    __tablename__ = 'board_columns'

    id = db.Column(db.Integer, primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    status_mapping = db.Column(db.String(30))  # Maps to task status
    color = db.Column(db.String(7), default='#6B7280')
    position = db.Column(db.Integer, default=0)
    wip_limit = db.Column(db.Integer)  # Work in progress limit

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    board = db.relationship('Board', back_populates='columns')

    def to_dict(self):
        return {
            'id': self.id,
            'board_id': self.board_id,
            'name': self.name,
            'status_mapping': self.status_mapping,
            'color': self.color,
            'position': self.position,
            'wip_limit': self.wip_limit,
            'task_count': self.get_task_count()
        }

    def get_task_count(self):
        """Get count of tasks in this column"""
        from app.models.task import Task
        return Task.query.filter_by(
            board_id=self.board_id,
            status=self.status_mapping
        ).count()

    def __repr__(self):
        return f'<BoardColumn {self.name}>'
