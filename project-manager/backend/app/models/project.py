"""
Project Model - Core project entity with baseline tracking
"""
from datetime import datetime
from app import db


class Project(db.Model):
    """Project model - core entity for project management"""
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    code = db.Column(db.String(20), unique=True)  # Project code like PRJ-001
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    template_id = db.Column(db.Integer, db.ForeignKey('templates.id'))

    # Status
    status = db.Column(db.String(20), default='planning')
    # planning, active, on_hold, at_risk, completed, cancelled
    priority = db.Column(db.String(10), default='medium')  # low, medium, high, critical
    health = db.Column(db.String(10), default='green')  # green, yellow, red

    # Timeline
    start_date = db.Column(db.Date)
    target_end_date = db.Column(db.Date)
    actual_end_date = db.Column(db.Date)

    # Budget
    budget = db.Column(db.Float, default=0.0)
    actual_cost = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(3), default='USD')

    # Progress
    progress = db.Column(db.Float, default=0.0)  # 0-100

    # Settings
    settings = db.Column(db.JSON, default=dict)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    program = db.relationship('Program', back_populates='projects')
    owner = db.relationship('User', backref='owned_projects')
    template = db.relationship('Template', backref='projects')
    boards = db.relationship('Board', back_populates='project', lazy='dynamic',
                            cascade='all, delete-orphan')
    milestones = db.relationship('Milestone', back_populates='project', lazy='dynamic',
                                cascade='all, delete-orphan')
    risks = db.relationship('Risk', back_populates='project', lazy='dynamic',
                           cascade='all, delete-orphan')
    baselines = db.relationship('ProjectBaseline', back_populates='project', lazy='dynamic',
                               cascade='all, delete-orphan')

    def to_dict(self, include_boards=False, include_milestones=False):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'code': self.code,
            'program_id': self.program_id,
            'owner_id': self.owner_id,
            'owner': self.owner.to_dict() if self.owner else None,
            'status': self.status,
            'priority': self.priority,
            'health': self.health,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'target_end_date': self.target_end_date.isoformat() if self.target_end_date else None,
            'actual_end_date': self.actual_end_date.isoformat() if self.actual_end_date else None,
            'budget': self.budget,
            'actual_cost': self.actual_cost,
            'currency': self.currency,
            'progress': self.get_progress(),
            'task_count': self.get_task_count(),
            'completed_task_count': self.get_completed_task_count(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        if include_boards:
            data['boards'] = [b.to_dict() for b in self.boards]
        if include_milestones:
            data['milestones'] = [m.to_dict() for m in self.milestones]
        return data

    def get_progress(self):
        """Calculate project progress based on tasks"""
        total_tasks = 0
        completed_tasks = 0
        for board in self.boards:
            for task in board.tasks:
                total_tasks += 1
                if task.status == 'completed':
                    completed_tasks += 1
        if total_tasks == 0:
            return 0
        return round((completed_tasks / total_tasks) * 100, 1)

    def get_task_count(self):
        """Get total task count"""
        count = 0
        for board in self.boards:
            count += board.tasks.count()
        return count

    def get_completed_task_count(self):
        """Get completed task count"""
        count = 0
        for board in self.boards:
            count += board.tasks.filter_by(status='completed').count()
        return count

    def create_baseline(self, name=None):
        """Create a baseline snapshot of current project state"""
        from app.models.task import Task

        baseline_data = {
            'project_info': {
                'start_date': self.start_date.isoformat() if self.start_date else None,
                'target_end_date': self.target_end_date.isoformat() if self.target_end_date else None,
                'budget': self.budget
            },
            'tasks': [],
            'milestones': []
        }

        for board in self.boards:
            for task in board.tasks:
                baseline_data['tasks'].append({
                    'id': task.id,
                    'title': task.title,
                    'start_date': task.start_date.isoformat() if task.start_date else None,
                    'due_date': task.due_date.isoformat() if task.due_date else None,
                    'estimated_hours': task.estimated_hours,
                    'status': task.status
                })

        for milestone in self.milestones:
            baseline_data['milestones'].append({
                'id': milestone.id,
                'name': milestone.name,
                'due_date': milestone.due_date.isoformat() if milestone.due_date else None,
                'status': milestone.status
            })

        baseline = ProjectBaseline(
            project_id=self.id,
            name=name or f'Baseline {datetime.utcnow().strftime("%Y-%m-%d")}',
            baseline_data=baseline_data
        )
        db.session.add(baseline)
        return baseline

    def __repr__(self):
        return f'<Project {self.name}>'


class ProjectBaseline(db.Model):
    """Baseline snapshots for comparing planned vs actual"""
    __tablename__ = 'project_baselines'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    baseline_data = db.Column(db.JSON, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Relationships
    project = db.relationship('Project', back_populates='baselines')
    created_by = db.relationship('User', backref='created_baselines')

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'baseline_data': self.baseline_data,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'created_by_id': self.created_by_id
        }

    def compare_with_current(self):
        """Compare baseline with current project state"""
        differences = {
            'timeline_variance': {},
            'task_changes': [],
            'milestone_changes': []
        }

        project = self.project
        baseline = self.baseline_data

        # Compare dates
        if baseline['project_info']['target_end_date'] and project.target_end_date:
            from datetime import date
            baseline_end = date.fromisoformat(baseline['project_info']['target_end_date'])
            variance_days = (project.target_end_date - baseline_end).days
            differences['timeline_variance']['end_date_variance_days'] = variance_days

        # Compare tasks
        baseline_tasks = {t['id']: t for t in baseline['tasks']}
        for board in project.boards:
            for task in board.tasks:
                if task.id in baseline_tasks:
                    bt = baseline_tasks[task.id]
                    if task.due_date and bt['due_date']:
                        baseline_due = date.fromisoformat(bt['due_date'])
                        if task.due_date != baseline_due:
                            differences['task_changes'].append({
                                'task_id': task.id,
                                'task_title': task.title,
                                'baseline_due': bt['due_date'],
                                'current_due': task.due_date.isoformat(),
                                'variance_days': (task.due_date - baseline_due).days
                            })

        return differences

    def __repr__(self):
        return f'<ProjectBaseline {self.name}>'


class Milestone(db.Model):
    """Project milestones"""
    __tablename__ = 'milestones'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    completed_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed, missed
    color = db.Column(db.String(7), default='#F59E0B')

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    project = db.relationship('Project', back_populates='milestones')

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'completed_date': self.completed_date.isoformat() if self.completed_date else None,
            'status': self.status,
            'color': self.color,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Milestone {self.name}>'
