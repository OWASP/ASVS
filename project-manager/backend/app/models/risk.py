"""
Risk and Issue Models
"""
from datetime import datetime
from app import db


class Risk(db.Model):
    """Risk model for risk management"""
    __tablename__ = 'risks'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    # Risk assessment
    category = db.Column(db.String(50))  # technical, resource, schedule, budget, external
    probability = db.Column(db.String(10), default='medium')  # very_low, low, medium, high, very_high
    impact = db.Column(db.String(10), default='medium')  # very_low, low, medium, high, very_high
    risk_score = db.Column(db.Float)  # Calculated from probability * impact

    # Status tracking
    status = db.Column(db.String(20), default='identified')
    # identified, analyzing, mitigating, monitoring, resolved, accepted, closed

    # Assignment
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Mitigation
    mitigation_plan = db.Column(db.Text)
    contingency_plan = db.Column(db.Text)
    response_strategy = db.Column(db.String(20))  # avoid, transfer, mitigate, accept

    # Impact areas
    affected_milestones = db.Column(db.JSON, default=list)  # List of milestone IDs
    affected_tasks = db.Column(db.JSON, default=list)  # List of task IDs

    # Timeline
    identified_date = db.Column(db.Date, default=datetime.utcnow().date)
    target_resolution_date = db.Column(db.Date)
    actual_resolution_date = db.Column(db.Date)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    project = db.relationship('Project', back_populates='risks')
    owner = db.relationship('User', back_populates='owned_risks')

    # Probability and impact mapping for score calculation
    PROBABILITY_VALUES = {
        'very_low': 1,
        'low': 2,
        'medium': 3,
        'high': 4,
        'very_high': 5
    }

    IMPACT_VALUES = {
        'very_low': 1,
        'low': 2,
        'medium': 3,
        'high': 4,
        'very_high': 5
    }

    def calculate_risk_score(self):
        """Calculate risk score from probability and impact"""
        prob_value = self.PROBABILITY_VALUES.get(self.probability, 3)
        impact_value = self.IMPACT_VALUES.get(self.impact, 3)
        self.risk_score = prob_value * impact_value
        return self.risk_score

    def get_risk_level(self):
        """Get risk level based on score"""
        if self.risk_score is None:
            self.calculate_risk_score()

        if self.risk_score <= 4:
            return 'low'
        elif self.risk_score <= 9:
            return 'medium'
        elif self.risk_score <= 15:
            return 'high'
        else:
            return 'critical'

    def to_dict(self):
        if self.risk_score is None:
            self.calculate_risk_score()

        return {
            'id': self.id,
            'project_id': self.project_id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'probability': self.probability,
            'impact': self.impact,
            'risk_score': self.risk_score,
            'risk_level': self.get_risk_level(),
            'status': self.status,
            'owner_id': self.owner_id,
            'owner': self.owner.to_dict() if self.owner else None,
            'mitigation_plan': self.mitigation_plan,
            'contingency_plan': self.contingency_plan,
            'response_strategy': self.response_strategy,
            'affected_milestones': self.affected_milestones,
            'affected_tasks': self.affected_tasks,
            'identified_date': self.identified_date.isoformat() if self.identified_date else None,
            'target_resolution_date': self.target_resolution_date.isoformat() if self.target_resolution_date else None,
            'actual_resolution_date': self.actual_resolution_date.isoformat() if self.actual_resolution_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Risk {self.title[:30]}>'


class Issue(db.Model):
    """Issue model for tracking problems that have occurred"""
    __tablename__ = 'issues'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    # Issue details
    category = db.Column(db.String(50))  # technical, process, resource, external
    severity = db.Column(db.String(10), default='medium')  # low, medium, high, critical
    priority = db.Column(db.String(10), default='medium')  # low, medium, high, urgent

    # Status tracking
    status = db.Column(db.String(20), default='open')
    # open, investigating, in_progress, resolved, closed, escalated

    # Assignment
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Resolution
    resolution = db.Column(db.Text)
    root_cause = db.Column(db.Text)

    # Related risk (if issue arose from a risk)
    related_risk_id = db.Column(db.Integer, db.ForeignKey('risks.id'))

    # Timeline
    reported_date = db.Column(db.Date, default=datetime.utcnow().date)
    target_resolution_date = db.Column(db.Date)
    actual_resolution_date = db.Column(db.Date)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    project = db.relationship('Project', backref='issues')
    owner = db.relationship('User', foreign_keys=[owner_id], backref='owned_issues')
    assigned_to = db.relationship('User', foreign_keys=[assigned_to_id], backref='assigned_issues')
    related_risk = db.relationship('Risk', backref='related_issues')

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'severity': self.severity,
            'priority': self.priority,
            'status': self.status,
            'owner_id': self.owner_id,
            'owner': self.owner.to_dict() if self.owner else None,
            'assigned_to_id': self.assigned_to_id,
            'assigned_to': self.assigned_to.to_dict() if self.assigned_to else None,
            'resolution': self.resolution,
            'root_cause': self.root_cause,
            'related_risk_id': self.related_risk_id,
            'reported_date': self.reported_date.isoformat() if self.reported_date else None,
            'target_resolution_date': self.target_resolution_date.isoformat() if self.target_resolution_date else None,
            'actual_resolution_date': self.actual_resolution_date.isoformat() if self.actual_resolution_date else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

    def __repr__(self):
        return f'<Issue {self.title[:30]}>'
