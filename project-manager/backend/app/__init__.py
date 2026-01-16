"""
Project Manager Application - Flask Backend
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_socketio import SocketIO

from app.config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
socketio = SocketIO()


def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    socketio.init_app(app, cors_allowed_origins="*", async_mode='eventlet')

    # Register blueprints
    from app.api.auth import auth_bp
    from app.api.users import users_bp
    from app.api.portfolios import portfolios_bp
    from app.api.programs import programs_bp
    from app.api.projects import projects_bp
    from app.api.boards import boards_bp
    from app.api.tasks import tasks_bp
    from app.api.risks import risks_bp
    from app.api.resources import resources_bp
    from app.api.automations import automations_bp
    from app.api.templates import templates_bp
    from app.api.reports import reports_bp

    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(users_bp, url_prefix='/api/v1/users')
    app.register_blueprint(portfolios_bp, url_prefix='/api/v1/portfolios')
    app.register_blueprint(programs_bp, url_prefix='/api/v1/programs')
    app.register_blueprint(projects_bp, url_prefix='/api/v1/projects')
    app.register_blueprint(boards_bp, url_prefix='/api/v1/boards')
    app.register_blueprint(tasks_bp, url_prefix='/api/v1/tasks')
    app.register_blueprint(risks_bp, url_prefix='/api/v1/risks')
    app.register_blueprint(resources_bp, url_prefix='/api/v1/resources')
    app.register_blueprint(automations_bp, url_prefix='/api/v1/automations')
    app.register_blueprint(templates_bp, url_prefix='/api/v1/templates')
    app.register_blueprint(reports_bp, url_prefix='/api/v1/reports')

    # Register WebSocket events
    from app.websocket import register_socket_events
    register_socket_events(socketio)

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
