"""
Template Models - Project and task templates
"""
from datetime import datetime
from app import db


class Template(db.Model):
    """Project templates for quick project setup"""
    __tablename__ = 'templates'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50))  # software, marketing, operations, hr, custom

    # Template configuration
    structure = db.Column(db.JSON, default=dict)
    # Contains: boards, columns, milestones, default settings

    # Metadata
    is_public = db.Column(db.Boolean, default=True)  # Available to all users
    is_system = db.Column(db.Boolean, default=False)  # Built-in template
    usage_count = db.Column(db.Integer, default=0)

    # Creator
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    created_by = db.relationship('User', backref='created_templates')
    tasks = db.relationship('TemplateTask', back_populates='template',
                           lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self, include_tasks=True):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'structure': self.structure,
            'is_public': self.is_public,
            'is_system': self.is_system,
            'usage_count': self.usage_count,
            'task_count': self.tasks.count(),
            'created_by_id': self.created_by_id,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
        if include_tasks:
            data['tasks'] = [t.to_dict() for t in self.tasks]
        return data

    def apply_to_project(self, project):
        """Apply template to a project"""
        from app.models.board import Board, BoardColumn
        from app.models.task import Task
        from app.models.project import Milestone

        # Create boards from template structure
        if 'boards' in self.structure:
            for board_data in self.structure['boards']:
                board = Board(
                    project_id=project.id,
                    name=board_data.get('name', 'Main Board'),
                    view_type=board_data.get('view_type', 'kanban'),
                    is_default=board_data.get('is_default', False)
                )
                db.session.add(board)
                db.session.flush()  # Get board ID

                # Create columns
                if 'columns' in board_data:
                    for i, col_data in enumerate(board_data['columns']):
                        column = BoardColumn(
                            board_id=board.id,
                            name=col_data.get('name'),
                            status_mapping=col_data.get('status_mapping'),
                            color=col_data.get('color', '#6B7280'),
                            position=i,
                            wip_limit=col_data.get('wip_limit')
                        )
                        db.session.add(column)
                else:
                    board.create_default_columns()

        # Create milestones from template
        if 'milestones' in self.structure:
            for ms_data in self.structure['milestones']:
                milestone = Milestone(
                    project_id=project.id,
                    name=ms_data.get('name'),
                    description=ms_data.get('description'),
                    color=ms_data.get('color', '#F59E0B')
                )
                db.session.add(milestone)

        # Create tasks from template tasks
        task_id_mapping = {}  # Map template task IDs to new task IDs
        default_board = project.boards.filter_by(is_default=True).first()
        if not default_board:
            default_board = project.boards.first()

        for template_task in self.tasks.order_by(TemplateTask.order):
            task = Task(
                board_id=default_board.id if default_board else None,
                title=template_task.title,
                description=template_task.description,
                status=template_task.default_status or 'todo',
                priority=template_task.default_priority or 'medium',
                task_type=template_task.task_type or 'task',
                estimated_hours=template_task.estimated_hours,
                position=template_task.order
            )
            db.session.add(task)
            db.session.flush()
            task_id_mapping[template_task.id] = task.id

        # Update usage count
        self.usage_count += 1

        return project

    def __repr__(self):
        return f'<Template {self.name}>'


class TemplateTask(db.Model):
    """Tasks within a template"""
    __tablename__ = 'template_tasks'

    id = db.Column(db.Integer, primary_key=True)
    template_id = db.Column(db.Integer, db.ForeignKey('templates.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    # Default values
    default_status = db.Column(db.String(30), default='todo')
    default_priority = db.Column(db.String(10), default='medium')
    task_type = db.Column(db.String(20), default='task')
    estimated_hours = db.Column(db.Float)

    # Relative timing (days from project start)
    relative_start_day = db.Column(db.Integer)
    relative_due_day = db.Column(db.Integer)

    # Ordering and hierarchy
    order = db.Column(db.Integer, default=0)
    parent_order = db.Column(db.Integer)  # Reference to parent template task

    # Dependencies (stored as list of template task orders)
    dependency_orders = db.Column(db.JSON, default=list)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    template = db.relationship('Template', back_populates='tasks')

    def to_dict(self):
        return {
            'id': self.id,
            'template_id': self.template_id,
            'title': self.title,
            'description': self.description,
            'default_status': self.default_status,
            'default_priority': self.default_priority,
            'task_type': self.task_type,
            'estimated_hours': self.estimated_hours,
            'relative_start_day': self.relative_start_day,
            'relative_due_day': self.relative_due_day,
            'order': self.order,
            'parent_order': self.parent_order,
            'dependency_orders': self.dependency_orders
        }

    def __repr__(self):
        return f'<TemplateTask {self.title[:30]}>'
