"""
Portfolio Model - Top-level organizational container
"""
from datetime import datetime
from app import db


class Portfolio(db.Model):
    """Portfolio model for grouping programs and projects"""
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default='active')  # active, on_hold, completed, archived
    color = db.Column(db.String(7), default='#6366F1')

    # Budget tracking
    total_budget = db.Column(db.Float, default=0.0)
    currency = db.Column(db.String(3), default='USD')

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owner = db.relationship('User', backref='owned_portfolios')
    programs = db.relationship('Program', back_populates='portfolio', lazy='dynamic')

    def to_dict(self, include_programs=False):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner_id,
            'owner': self.owner.to_dict() if self.owner else None,
            'status': self.status,
            'color': self.color,
            'total_budget': self.total_budget,
            'currency': self.currency,
            'program_count': self.programs.count(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        if include_programs:
            data['programs'] = [p.to_dict() for p in self.programs]
        return data

    def get_dashboard_stats(self):
        """Get aggregated statistics for dashboard"""
        total_projects = 0
        completed_projects = 0
        at_risk_projects = 0
        total_spent = 0.0

        for program in self.programs:
            for project in program.projects:
                total_projects += 1
                if project.status == 'completed':
                    completed_projects += 1
                if project.status == 'at_risk':
                    at_risk_projects += 1
                total_spent += project.actual_cost or 0

        return {
            'total_programs': self.programs.count(),
            'total_projects': total_projects,
            'completed_projects': completed_projects,
            'at_risk_projects': at_risk_projects,
            'total_budget': self.total_budget,
            'total_spent': total_spent,
            'budget_utilization': (total_spent / self.total_budget * 100) if self.total_budget > 0 else 0
        }

    def __repr__(self):
        return f'<Portfolio {self.name}>'
