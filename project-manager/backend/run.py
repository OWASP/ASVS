"""
Application Entry Point
"""
import os
from app import create_app, socketio, db
from app.config import config

# Get environment
env = os.environ.get('FLASK_ENV', 'development')
app = create_app(config.get(env, config['default']))


@app.cli.command('init-db')
def init_db():
    """Initialize the database with tables and seed data"""
    with app.app_context():
        db.create_all()
        print('Database tables created.')

        # Seed system templates
        from app.models import Template
        if Template.query.filter_by(is_system=True).count() == 0:
            _seed_system_templates()
            print('System templates seeded.')

        # Create default admin user if none exists
        from app.models import User
        if User.query.count() == 0:
            admin = User(
                email='admin@projectmanager.local',
                name='Admin User',
                role='admin'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print('Default admin user created (admin@projectmanager.local / admin123)')


def _seed_system_templates():
    """Seed system templates"""
    from app.models import Template, TemplateTask

    templates_data = [
        {
            'name': 'Agile Sprint',
            'description': 'Two-week agile sprint with standard ceremonies',
            'category': 'software',
            'is_system': True,
            'structure': {
                'boards': [{
                    'name': 'Sprint Board',
                    'view_type': 'kanban',
                    'is_default': True,
                    'columns': [
                        {'name': 'Backlog', 'status_mapping': 'backlog', 'color': '#6B7280'},
                        {'name': 'To Do', 'status_mapping': 'todo', 'color': '#3B82F6'},
                        {'name': 'In Progress', 'status_mapping': 'in_progress', 'color': '#F59E0B'},
                        {'name': 'Review', 'status_mapping': 'review', 'color': '#8B5CF6'},
                        {'name': 'Done', 'status_mapping': 'completed', 'color': '#10B981'}
                    ]
                }]
            }
        },
        {
            'name': 'Marketing Campaign',
            'description': 'Marketing campaign template with content workflow',
            'category': 'marketing',
            'is_system': True,
            'structure': {
                'boards': [{
                    'name': 'Campaign Board',
                    'view_type': 'kanban',
                    'is_default': True,
                    'columns': [
                        {'name': 'Ideas', 'status_mapping': 'backlog', 'color': '#6B7280'},
                        {'name': 'Planning', 'status_mapping': 'todo', 'color': '#3B82F6'},
                        {'name': 'Creating', 'status_mapping': 'in_progress', 'color': '#F59E0B'},
                        {'name': 'Review', 'status_mapping': 'review', 'color': '#8B5CF6'},
                        {'name': 'Published', 'status_mapping': 'completed', 'color': '#10B981'}
                    ]
                }]
            }
        }
    ]

    for tmpl_data in templates_data:
        template = Template(
            name=tmpl_data['name'],
            description=tmpl_data['description'],
            category=tmpl_data['category'],
            structure=tmpl_data['structure'],
            is_public=True,
            is_system=True
        )
        db.session.add(template)

    db.session.commit()


if __name__ == '__main__':
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Create uploads directory
    upload_dir = os.path.join(os.path.dirname(__file__), 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Run with SocketIO for WebSocket support
    socketio.run(
        app,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=app.config['DEBUG']
    )
