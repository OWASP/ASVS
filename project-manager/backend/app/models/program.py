"""
Program Model - Container for related projects with OKR alignment
"""
from datetime import datetime
from app import db


class Program(db.Model):
    """Program model for grouping related projects"""
    __tablename__ = 'programs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'))
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default='planning')  # planning, active, on_hold, completed
    color = db.Column(db.String(7), default='#8B5CF6')

    # Timeline
    start_date = db.Column(db.Date)
    target_end_date = db.Column(db.Date)
    actual_end_date = db.Column(db.Date)

    # Budget
    budget = db.Column(db.Float, default=0.0)
    actual_cost = db.Column(db.Float, default=0.0)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    portfolio = db.relationship('Portfolio', back_populates='programs')
    owner = db.relationship('User', backref='owned_programs')
    projects = db.relationship('Project', back_populates='program', lazy='dynamic')
    okrs = db.relationship('OKR', back_populates='program', lazy='dynamic', cascade='all, delete-orphan')

    def to_dict(self, include_projects=False, include_okrs=False):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'portfolio_id': self.portfolio_id,
            'owner_id': self.owner_id,
            'owner': self.owner.to_dict() if self.owner else None,
            'status': self.status,
            'color': self.color,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'target_end_date': self.target_end_date.isoformat() if self.target_end_date else None,
            'actual_end_date': self.actual_end_date.isoformat() if self.actual_end_date else None,
            'budget': self.budget,
            'actual_cost': self.actual_cost,
            'project_count': self.projects.count(),
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        if include_projects:
            data['projects'] = [p.to_dict() for p in self.projects]
        if include_okrs:
            data['okrs'] = [o.to_dict() for o in self.okrs]
        return data

    def get_progress(self):
        """Calculate overall program progress"""
        projects = list(self.projects)
        if not projects:
            return 0
        total_progress = sum(p.get_progress() for p in projects)
        return total_progress / len(projects)

    def __repr__(self):
        return f'<Program {self.name}>'


class OKR(db.Model):
    """Objectives and Key Results model"""
    __tablename__ = 'okrs'

    id = db.Column(db.Integer, primary_key=True)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)
    objective = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default='on_track')  # on_track, at_risk, behind, completed
    quarter = db.Column(db.String(10))  # Q1-2024, Q2-2024, etc.
    year = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    program = db.relationship('Program', back_populates='okrs')
    owner = db.relationship('User', backref='owned_okrs')
    key_results = db.relationship('KeyResult', back_populates='okr', lazy='dynamic',
                                  cascade='all, delete-orphan')

    def to_dict(self, include_key_results=True):
        data = {
            'id': self.id,
            'program_id': self.program_id,
            'objective': self.objective,
            'description': self.description,
            'owner_id': self.owner_id,
            'status': self.status,
            'quarter': self.quarter,
            'year': self.year,
            'progress': self.get_progress(),
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
        if include_key_results:
            data['key_results'] = [kr.to_dict() for kr in self.key_results]
        return data

    def get_progress(self):
        """Calculate OKR progress based on key results"""
        key_results = list(self.key_results)
        if not key_results:
            return 0
        total_progress = sum(kr.progress for kr in key_results)
        return total_progress / len(key_results)

    def __repr__(self):
        return f'<OKR {self.objective[:50]}>'


class KeyResult(db.Model):
    """Key Results for OKRs"""
    __tablename__ = 'key_results'

    id = db.Column(db.Integer, primary_key=True)
    okr_id = db.Column(db.Integer, db.ForeignKey('okrs.id'), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    metric_type = db.Column(db.String(20), default='percentage')  # percentage, number, currency, boolean
    target_value = db.Column(db.Float, default=100.0)
    current_value = db.Column(db.Float, default=0.0)
    unit = db.Column(db.String(20))  # %, $, users, etc.

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    okr = db.relationship('OKR', back_populates='key_results')

    @property
    def progress(self):
        """Calculate progress percentage"""
        if self.metric_type == 'boolean':
            return 100 if self.current_value >= 1 else 0
        if self.target_value == 0:
            return 0
        return min(100, (self.current_value / self.target_value) * 100)

    def to_dict(self):
        return {
            'id': self.id,
            'okr_id': self.okr_id,
            'description': self.description,
            'metric_type': self.metric_type,
            'target_value': self.target_value,
            'current_value': self.current_value,
            'unit': self.unit,
            'progress': self.progress,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<KeyResult {self.description[:30]}>'
