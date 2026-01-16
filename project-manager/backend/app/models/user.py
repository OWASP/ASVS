"""
User and Team Models
"""
from datetime import datetime
from app import db
import bcrypt


class User(db.Model):
    """User model for authentication and resource management"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    avatar_url = db.Column(db.String(255))
    role = db.Column(db.String(20), default='member')  # admin, manager, member
    is_active = db.Column(db.Boolean, default=True)

    # Capacity and scheduling
    weekly_capacity_hours = db.Column(db.Float, default=40.0)
    working_hours_start = db.Column(db.String(5), default='09:00')
    working_hours_end = db.Column(db.String(5), default='17:00')
    timezone = db.Column(db.String(50), default='UTC')

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    # Relationships
    skills = db.relationship('UserSkill', back_populates='user', lazy='dynamic')
    team_memberships = db.relationship('TeamMember', back_populates='user', lazy='dynamic')
    assigned_tasks = db.relationship('Task', back_populates='assignee', lazy='dynamic',
                                     foreign_keys='Task.assignee_id')
    owned_risks = db.relationship('Risk', back_populates='owner', lazy='dynamic')
    time_entries = db.relationship('TimeEntry', back_populates='user', lazy='dynamic')
    comments = db.relationship('Comment', back_populates='author', lazy='dynamic')
    notifications = db.relationship('Notification', back_populates='user', lazy='dynamic')

    def set_password(self, password):
        """Hash and set password"""
        self.password_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

    def check_password(self, password):
        """Verify password"""
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password_hash.encode('utf-8')
        )

    def to_dict(self, include_sensitive=False):
        """Convert to dictionary"""
        data = {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'avatar_url': self.avatar_url,
            'role': self.role,
            'is_active': self.is_active,
            'weekly_capacity_hours': self.weekly_capacity_hours,
            'working_hours_start': self.working_hours_start,
            'working_hours_end': self.working_hours_end,
            'timezone': self.timezone,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'skills': [us.skill.name for us in self.skills]
        }
        return data

    def __repr__(self):
        return f'<User {self.email}>'


class Team(db.Model):
    """Team model for grouping users"""
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    color = db.Column(db.String(7), default='#3B82F6')  # Hex color

    # Capacity rules
    default_capacity_hours = db.Column(db.Float, default=40.0)
    holidays = db.Column(db.JSON, default=list)  # List of holiday dates

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    members = db.relationship('TeamMember', back_populates='team', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'color': self.color,
            'default_capacity_hours': self.default_capacity_hours,
            'holidays': self.holidays,
            'member_count': self.members.count(),
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f'<Team {self.name}>'


class TeamMember(db.Model):
    """Association table for team membership"""
    __tablename__ = 'team_members'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(20), default='member')  # lead, member
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    team = db.relationship('Team', back_populates='members')
    user = db.relationship('User', back_populates='team_memberships')

    __table_args__ = (
        db.UniqueConstraint('team_id', 'user_id', name='unique_team_member'),
    )


class Skill(db.Model):
    """Skill model for skill-based assignment"""
    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    category = db.Column(db.String(50))  # technical, soft, domain
    description = db.Column(db.Text)

    # Relationships
    users = db.relationship('UserSkill', back_populates='skill', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description
        }

    def __repr__(self):
        return f'<Skill {self.name}>'


class UserSkill(db.Model):
    """Association table for user skills with proficiency"""
    __tablename__ = 'user_skills'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.id'), nullable=False)
    proficiency = db.Column(db.Integer, default=3)  # 1-5 scale

    # Relationships
    user = db.relationship('User', back_populates='skills')
    skill = db.relationship('Skill', back_populates='users')

    __table_args__ = (
        db.UniqueConstraint('user_id', 'skill_id', name='unique_user_skill'),
    )
