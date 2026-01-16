"""
Automations API endpoints
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Automation, AutomationAction, AutomationLog

automations_bp = Blueprint('automations', __name__)


@automations_bp.route('', methods=['GET'])
@jwt_required()
def get_automations():
    """Get all automations"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    scope_type = request.args.get('scope_type')
    scope_id = request.args.get('scope_id', type=int)
    is_active = request.args.get('is_active')

    query = Automation.query

    if scope_type:
        query = query.filter_by(scope_type=scope_type)
    if scope_id:
        query = query.filter_by(scope_id=scope_id)
    if is_active is not None:
        query = query.filter_by(is_active=is_active.lower() == 'true')

    pagination = query.order_by(Automation.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'automations': [a.to_dict() for a in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@automations_bp.route('', methods=['POST'])
@jwt_required()
def create_automation():
    """Create a new automation"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Automation name is required'}), 400
    if not data.get('trigger_type'):
        return jsonify({'error': 'trigger_type is required'}), 400

    automation = Automation(
        name=data['name'],
        description=data.get('description'),
        scope_type=data.get('scope_type', 'project'),
        scope_id=data.get('scope_id'),
        trigger_type=data['trigger_type'],
        trigger_conditions=data.get('trigger_conditions', {}),
        is_active=data.get('is_active', True),
        created_by_id=user_id
    )
    db.session.add(automation)
    db.session.flush()

    # Add actions
    if data.get('actions'):
        for i, action_data in enumerate(data['actions']):
            action = AutomationAction(
                automation_id=automation.id,
                action_type=action_data['action_type'],
                action_config=action_data.get('action_config', {}),
                order=i,
                stop_on_error=action_data.get('stop_on_error', False)
            )
            db.session.add(action)

    db.session.commit()
    return jsonify(automation.to_dict()), 201


@automations_bp.route('/<int:automation_id>', methods=['GET'])
@jwt_required()
def get_automation(automation_id):
    """Get a specific automation"""
    automation = Automation.query.get_or_404(automation_id)
    return jsonify(automation.to_dict()), 200


@automations_bp.route('/<int:automation_id>', methods=['PUT'])
@jwt_required()
def update_automation(automation_id):
    """Update an automation"""
    automation = Automation.query.get_or_404(automation_id)
    data = request.get_json()

    allowed_fields = ['name', 'description', 'scope_type', 'scope_id',
                      'trigger_type', 'trigger_conditions', 'is_active']

    for field in allowed_fields:
        if field in data:
            setattr(automation, field, data[field])

    # Update actions if provided
    if 'actions' in data:
        # Remove existing actions
        AutomationAction.query.filter_by(automation_id=automation_id).delete()

        # Add new actions
        for i, action_data in enumerate(data['actions']):
            action = AutomationAction(
                automation_id=automation_id,
                action_type=action_data['action_type'],
                action_config=action_data.get('action_config', {}),
                order=i,
                stop_on_error=action_data.get('stop_on_error', False)
            )
            db.session.add(action)

    db.session.commit()
    return jsonify(automation.to_dict()), 200


@automations_bp.route('/<int:automation_id>', methods=['DELETE'])
@jwt_required()
def delete_automation(automation_id):
    """Delete an automation"""
    automation = Automation.query.get_or_404(automation_id)
    db.session.delete(automation)
    db.session.commit()
    return jsonify({'message': 'Automation deleted'}), 200


@automations_bp.route('/<int:automation_id>/test', methods=['POST'])
@jwt_required()
def test_automation(automation_id):
    """Test an automation with sample data"""
    automation = Automation.query.get_or_404(automation_id)
    data = request.get_json()

    # Simulate execution without actually making changes
    test_context = data.get('context', {})
    test_context['_test_mode'] = True

    results = {
        'automation_id': automation_id,
        'would_trigger': automation.check_conditions(type('obj', (object,), test_context)()),
        'actions_count': automation.actions.count(),
        'actions': [
            {
                'action_type': a.action_type,
                'action_config': a.action_config,
                'order': a.order
            } for a in automation.actions
        ]
    }

    return jsonify(results), 200


@automations_bp.route('/<int:automation_id>/toggle', methods=['POST'])
@jwt_required()
def toggle_automation(automation_id):
    """Toggle automation active state"""
    automation = Automation.query.get_or_404(automation_id)
    automation.is_active = not automation.is_active
    db.session.commit()
    return jsonify({
        'message': f'Automation {"activated" if automation.is_active else "deactivated"}',
        'is_active': automation.is_active
    }), 200


@automations_bp.route('/<int:automation_id>/logs', methods=['GET'])
@jwt_required()
def get_automation_logs(automation_id):
    """Get automation execution logs"""
    automation = Automation.query.get_or_404(automation_id)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)

    pagination = automation.logs.order_by(AutomationLog.executed_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'logs': [l.to_dict() for l in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


# Predefined automation templates/recipes
@automations_bp.route('/recipes', methods=['GET'])
@jwt_required()
def get_recipes():
    """Get predefined automation recipes"""
    recipes = [
        {
            'id': 'task_completed_notify',
            'name': 'Notify on Task Completion',
            'description': 'Send notification when a task is completed',
            'trigger_type': 'task_status_changed',
            'trigger_conditions': {'status': 'completed'},
            'actions': [
                {
                    'action_type': 'send_notification',
                    'action_config': {
                        'to': 'task_reporter',
                        'template': 'task_completed'
                    }
                }
            ]
        },
        {
            'id': 'due_date_reminder',
            'name': 'Due Date Reminder',
            'description': 'Send reminder when due date is approaching',
            'trigger_type': 'due_date_approaching',
            'trigger_conditions': {'days_before': 2},
            'actions': [
                {
                    'action_type': 'send_notification',
                    'action_config': {
                        'to': 'task_assignee',
                        'template': 'due_date_reminder'
                    }
                }
            ]
        },
        {
            'id': 'auto_assign_review',
            'name': 'Auto-assign for Review',
            'description': 'Assign task to reviewer when moved to review',
            'trigger_type': 'task_status_changed',
            'trigger_conditions': {'status': 'review'},
            'actions': [
                {
                    'action_type': 'assign_user',
                    'action_config': {
                        'user_type': 'project_owner'
                    }
                }
            ]
        },
        {
            'id': 'high_risk_alert',
            'name': 'High Risk Alert',
            'description': 'Alert when risk becomes high',
            'trigger_type': 'risk_status_changed',
            'trigger_conditions': {'risk_level': ['high', 'critical']},
            'actions': [
                {
                    'action_type': 'send_notification',
                    'action_config': {
                        'to': 'project_owner',
                        'priority': 'high',
                        'template': 'high_risk_alert'
                    }
                }
            ]
        },
        {
            'id': 'blocked_task_escalation',
            'name': 'Blocked Task Escalation',
            'description': 'Escalate when task is blocked for too long',
            'trigger_type': 'task_status_changed',
            'trigger_conditions': {'status': 'blocked'},
            'actions': [
                {
                    'action_type': 'send_notification',
                    'action_config': {
                        'to': 'project_owner',
                        'template': 'blocked_task'
                    }
                },
                {
                    'action_type': 'add_comment',
                    'action_config': {
                        'content': 'Task has been blocked. Please review and take action.'
                    }
                }
            ]
        }
    ]

    return jsonify(recipes), 200


@automations_bp.route('/recipes/<recipe_id>/apply', methods=['POST'])
@jwt_required()
def apply_recipe(recipe_id):
    """Apply a recipe to create an automation"""
    user_id = get_jwt_identity()
    data = request.get_json()

    # Get recipe (in production, these would be stored)
    recipes = {
        'task_completed_notify': {
            'name': 'Notify on Task Completion',
            'trigger_type': 'task_status_changed',
            'trigger_conditions': {'status': 'completed'},
            'actions': [{'action_type': 'send_notification', 'action_config': {'to': 'task_reporter', 'template': 'task_completed'}}]
        },
        'due_date_reminder': {
            'name': 'Due Date Reminder',
            'trigger_type': 'due_date_approaching',
            'trigger_conditions': {'days_before': 2},
            'actions': [{'action_type': 'send_notification', 'action_config': {'to': 'task_assignee', 'template': 'due_date_reminder'}}]
        }
    }

    recipe = recipes.get(recipe_id)
    if not recipe:
        return jsonify({'error': 'Recipe not found'}), 404

    automation = Automation(
        name=data.get('name', recipe['name']),
        description=data.get('description'),
        scope_type=data.get('scope_type', 'project'),
        scope_id=data.get('scope_id'),
        trigger_type=recipe['trigger_type'],
        trigger_conditions=recipe['trigger_conditions'],
        is_active=True,
        created_by_id=user_id
    )
    db.session.add(automation)
    db.session.flush()

    for i, action_data in enumerate(recipe['actions']):
        action = AutomationAction(
            automation_id=automation.id,
            action_type=action_data['action_type'],
            action_config=action_data['action_config'],
            order=i
        )
        db.session.add(action)

    db.session.commit()
    return jsonify(automation.to_dict()), 201
