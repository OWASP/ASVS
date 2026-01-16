"""
Templates API endpoints
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Template, TemplateTask, Project

templates_bp = Blueprint('templates', __name__)


@templates_bp.route('', methods=['GET'])
@jwt_required()
def get_templates():
    """Get all templates"""
    category = request.args.get('category')
    is_public = request.args.get('is_public')

    query = Template.query

    if category:
        query = query.filter_by(category=category)
    if is_public is not None:
        query = query.filter_by(is_public=is_public.lower() == 'true')

    templates = query.order_by(Template.usage_count.desc()).all()
    return jsonify([t.to_dict(include_tasks=False) for t in templates]), 200


@templates_bp.route('', methods=['POST'])
@jwt_required()
def create_template():
    """Create a new template"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Template name is required'}), 400

    template = Template(
        name=data['name'],
        description=data.get('description'),
        category=data.get('category', 'custom'),
        structure=data.get('structure', {}),
        is_public=data.get('is_public', True),
        created_by_id=user_id
    )
    db.session.add(template)
    db.session.flush()

    # Add template tasks
    if data.get('tasks'):
        for i, task_data in enumerate(data['tasks']):
            template_task = TemplateTask(
                template_id=template.id,
                title=task_data['title'],
                description=task_data.get('description'),
                default_status=task_data.get('default_status', 'todo'),
                default_priority=task_data.get('default_priority', 'medium'),
                task_type=task_data.get('task_type', 'task'),
                estimated_hours=task_data.get('estimated_hours'),
                relative_start_day=task_data.get('relative_start_day'),
                relative_due_day=task_data.get('relative_due_day'),
                order=i,
                parent_order=task_data.get('parent_order'),
                dependency_orders=task_data.get('dependency_orders', [])
            )
            db.session.add(template_task)

    db.session.commit()
    return jsonify(template.to_dict()), 201


@templates_bp.route('/<int:template_id>', methods=['GET'])
@jwt_required()
def get_template(template_id):
    """Get a specific template"""
    template = Template.query.get_or_404(template_id)
    return jsonify(template.to_dict()), 200


@templates_bp.route('/<int:template_id>', methods=['PUT'])
@jwt_required()
def update_template(template_id):
    """Update a template"""
    template = Template.query.get_or_404(template_id)
    data = request.get_json()

    allowed_fields = ['name', 'description', 'category', 'structure', 'is_public']
    for field in allowed_fields:
        if field in data:
            setattr(template, field, data[field])

    # Update tasks if provided
    if 'tasks' in data:
        # Remove existing tasks
        TemplateTask.query.filter_by(template_id=template_id).delete()

        # Add new tasks
        for i, task_data in enumerate(data['tasks']):
            template_task = TemplateTask(
                template_id=template_id,
                title=task_data['title'],
                description=task_data.get('description'),
                default_status=task_data.get('default_status', 'todo'),
                default_priority=task_data.get('default_priority', 'medium'),
                task_type=task_data.get('task_type', 'task'),
                estimated_hours=task_data.get('estimated_hours'),
                relative_start_day=task_data.get('relative_start_day'),
                relative_due_day=task_data.get('relative_due_day'),
                order=i,
                parent_order=task_data.get('parent_order'),
                dependency_orders=task_data.get('dependency_orders', [])
            )
            db.session.add(template_task)

    db.session.commit()
    return jsonify(template.to_dict()), 200


@templates_bp.route('/<int:template_id>', methods=['DELETE'])
@jwt_required()
def delete_template(template_id):
    """Delete a template"""
    template = Template.query.get_or_404(template_id)

    if template.is_system:
        return jsonify({'error': 'Cannot delete system template'}), 403

    db.session.delete(template)
    db.session.commit()
    return jsonify({'message': 'Template deleted'}), 200


@templates_bp.route('/<int:template_id>/apply', methods=['POST'])
@jwt_required()
def apply_template(template_id):
    """Apply template to a project"""
    template = Template.query.get_or_404(template_id)
    data = request.get_json()

    project_id = data.get('project_id')
    if not project_id:
        return jsonify({'error': 'project_id is required'}), 400

    project = Project.query.get_or_404(project_id)
    template.apply_to_project(project)
    db.session.commit()

    return jsonify({
        'message': 'Template applied successfully',
        'project': project.to_dict(include_boards=True)
    }), 200


@templates_bp.route('/from-project/<int:project_id>', methods=['POST'])
@jwt_required()
def create_from_project(project_id):
    """Create a template from an existing project"""
    user_id = get_jwt_identity()
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    # Build structure from project
    structure = {
        'boards': [],
        'milestones': []
    }

    for board in project.boards:
        board_data = {
            'name': board.name,
            'view_type': board.view_type,
            'is_default': board.is_default,
            'columns': [
                {
                    'name': col.name,
                    'status_mapping': col.status_mapping,
                    'color': col.color,
                    'wip_limit': col.wip_limit
                } for col in board.columns
            ]
        }
        structure['boards'].append(board_data)

    for milestone in project.milestones:
        structure['milestones'].append({
            'name': milestone.name,
            'description': milestone.description,
            'color': milestone.color
        })

    # Create template
    template = Template(
        name=data.get('name', f'{project.name} Template'),
        description=data.get('description', f'Template created from project {project.name}'),
        category=data.get('category', 'custom'),
        structure=structure,
        is_public=data.get('is_public', True),
        created_by_id=user_id
    )
    db.session.add(template)
    db.session.flush()

    # Add tasks as template tasks
    order = 0
    for board in project.boards:
        for task in board.tasks:
            template_task = TemplateTask(
                template_id=template.id,
                title=task.title,
                description=task.description,
                default_status='todo',  # Reset status
                default_priority=task.priority,
                task_type=task.task_type,
                estimated_hours=task.estimated_hours,
                order=order
            )
            db.session.add(template_task)
            order += 1

    db.session.commit()
    return jsonify(template.to_dict()), 201


# System templates (pre-built)
@templates_bp.route('/system', methods=['GET'])
@jwt_required()
def get_system_templates():
    """Get system templates"""
    templates = Template.query.filter_by(is_system=True).all()
    return jsonify([t.to_dict(include_tasks=False) for t in templates]), 200


@templates_bp.route('/seed-system', methods=['POST'])
@jwt_required()
def seed_system_templates():
    """Seed system templates (admin only)"""
    # Check if already seeded
    if Template.query.filter_by(is_system=True).count() > 0:
        return jsonify({'message': 'System templates already exist'}), 200

    system_templates = [
        {
            'name': 'Software Development Sprint',
            'description': 'Two-week agile sprint template with standard ceremonies',
            'category': 'software',
            'structure': {
                'boards': [
                    {
                        'name': 'Sprint Board',
                        'view_type': 'kanban',
                        'is_default': True,
                        'columns': [
                            {'name': 'Backlog', 'status_mapping': 'backlog', 'color': '#6B7280'},
                            {'name': 'To Do', 'status_mapping': 'todo', 'color': '#3B82F6'},
                            {'name': 'In Progress', 'status_mapping': 'in_progress', 'color': '#F59E0B'},
                            {'name': 'Code Review', 'status_mapping': 'review', 'color': '#8B5CF6'},
                            {'name': 'Testing', 'status_mapping': 'testing', 'color': '#EC4899'},
                            {'name': 'Done', 'status_mapping': 'completed', 'color': '#10B981'}
                        ]
                    }
                ],
                'milestones': [
                    {'name': 'Sprint Planning', 'color': '#3B82F6'},
                    {'name': 'Sprint Review', 'color': '#10B981'},
                    {'name': 'Sprint Retrospective', 'color': '#8B5CF6'}
                ]
            },
            'tasks': [
                {'title': 'Sprint Planning Meeting', 'task_type': 'task', 'estimated_hours': 2},
                {'title': 'Daily Standup', 'task_type': 'task', 'estimated_hours': 0.5},
                {'title': 'Sprint Review', 'task_type': 'task', 'estimated_hours': 1},
                {'title': 'Sprint Retrospective', 'task_type': 'task', 'estimated_hours': 1}
            ]
        },
        {
            'name': 'Marketing Campaign',
            'description': 'Marketing campaign launch template',
            'category': 'marketing',
            'structure': {
                'boards': [
                    {
                        'name': 'Campaign Board',
                        'view_type': 'kanban',
                        'is_default': True,
                        'columns': [
                            {'name': 'Ideas', 'status_mapping': 'backlog', 'color': '#6B7280'},
                            {'name': 'Planning', 'status_mapping': 'todo', 'color': '#3B82F6'},
                            {'name': 'Creating', 'status_mapping': 'in_progress', 'color': '#F59E0B'},
                            {'name': 'Review', 'status_mapping': 'review', 'color': '#8B5CF6'},
                            {'name': 'Scheduled', 'status_mapping': 'scheduled', 'color': '#EC4899'},
                            {'name': 'Published', 'status_mapping': 'completed', 'color': '#10B981'}
                        ]
                    }
                ],
                'milestones': [
                    {'name': 'Campaign Launch', 'color': '#EF4444'},
                    {'name': 'Mid-Campaign Review', 'color': '#F59E0B'},
                    {'name': 'Campaign Wrap-up', 'color': '#10B981'}
                ]
            },
            'tasks': [
                {'title': 'Define Campaign Goals', 'task_type': 'task', 'estimated_hours': 4},
                {'title': 'Identify Target Audience', 'task_type': 'task', 'estimated_hours': 3},
                {'title': 'Create Content Calendar', 'task_type': 'task', 'estimated_hours': 4},
                {'title': 'Design Creative Assets', 'task_type': 'task', 'estimated_hours': 8},
                {'title': 'Set Up Analytics', 'task_type': 'task', 'estimated_hours': 2}
            ]
        },
        {
            'name': 'Product Launch',
            'description': 'Product launch project template',
            'category': 'operations',
            'structure': {
                'boards': [
                    {
                        'name': 'Launch Board',
                        'view_type': 'kanban',
                        'is_default': True,
                        'columns': [
                            {'name': 'Not Started', 'status_mapping': 'todo', 'color': '#6B7280'},
                            {'name': 'In Progress', 'status_mapping': 'in_progress', 'color': '#F59E0B'},
                            {'name': 'Blocked', 'status_mapping': 'blocked', 'color': '#EF4444'},
                            {'name': 'Complete', 'status_mapping': 'completed', 'color': '#10B981'}
                        ]
                    }
                ],
                'milestones': [
                    {'name': 'Alpha Release', 'color': '#3B82F6'},
                    {'name': 'Beta Release', 'color': '#8B5CF6'},
                    {'name': 'GA Launch', 'color': '#10B981'}
                ]
            },
            'tasks': [
                {'title': 'Market Research', 'task_type': 'task', 'estimated_hours': 20},
                {'title': 'Product Requirements', 'task_type': 'task', 'estimated_hours': 16},
                {'title': 'Design Mockups', 'task_type': 'task', 'estimated_hours': 24},
                {'title': 'Development', 'task_type': 'epic', 'estimated_hours': 160},
                {'title': 'QA Testing', 'task_type': 'task', 'estimated_hours': 40},
                {'title': 'Documentation', 'task_type': 'task', 'estimated_hours': 16},
                {'title': 'Launch Preparation', 'task_type': 'task', 'estimated_hours': 8}
            ]
        }
    ]

    for tmpl_data in system_templates:
        template = Template(
            name=tmpl_data['name'],
            description=tmpl_data['description'],
            category=tmpl_data['category'],
            structure=tmpl_data['structure'],
            is_public=True,
            is_system=True
        )
        db.session.add(template)
        db.session.flush()

        for i, task_data in enumerate(tmpl_data.get('tasks', [])):
            template_task = TemplateTask(
                template_id=template.id,
                title=task_data['title'],
                task_type=task_data.get('task_type', 'task'),
                estimated_hours=task_data.get('estimated_hours'),
                order=i
            )
            db.session.add(template_task)

    db.session.commit()
    return jsonify({'message': 'System templates seeded successfully'}), 201
