"""
Risks and Issues API endpoints
"""
from datetime import datetime
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Risk, Issue

risks_bp = Blueprint('risks', __name__)


@risks_bp.route('', methods=['GET'])
@jwt_required()
def get_risks():
    """Get all risks with filtering"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    project_id = request.args.get('project_id', type=int)
    status = request.args.get('status')
    category = request.args.get('category')
    owner_id = request.args.get('owner_id', type=int)

    query = Risk.query

    if project_id:
        query = query.filter_by(project_id=project_id)
    if status:
        query = query.filter_by(status=status)
    if category:
        query = query.filter_by(category=category)
    if owner_id:
        query = query.filter_by(owner_id=owner_id)

    pagination = query.order_by(Risk.risk_score.desc().nullslast()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'risks': [r.to_dict() for r in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@risks_bp.route('', methods=['POST'])
@jwt_required()
def create_risk():
    """Create a new risk"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('project_id'):
        return jsonify({'error': 'project_id is required'}), 400
    if not data.get('title'):
        return jsonify({'error': 'Risk title is required'}), 400

    risk = Risk(
        project_id=data['project_id'],
        title=data['title'],
        description=data.get('description'),
        category=data.get('category'),
        probability=data.get('probability', 'medium'),
        impact=data.get('impact', 'medium'),
        status=data.get('status', 'identified'),
        owner_id=data.get('owner_id', user_id),
        mitigation_plan=data.get('mitigation_plan'),
        contingency_plan=data.get('contingency_plan'),
        response_strategy=data.get('response_strategy'),
        affected_milestones=data.get('affected_milestones', []),
        affected_tasks=data.get('affected_tasks', [])
    )

    if data.get('target_resolution_date'):
        risk.target_resolution_date = datetime.fromisoformat(data['target_resolution_date']).date()

    risk.calculate_risk_score()
    db.session.add(risk)
    db.session.commit()

    return jsonify(risk.to_dict()), 201


@risks_bp.route('/<int:risk_id>', methods=['GET'])
@jwt_required()
def get_risk(risk_id):
    """Get a specific risk"""
    risk = Risk.query.get_or_404(risk_id)
    return jsonify(risk.to_dict()), 200


@risks_bp.route('/<int:risk_id>', methods=['PUT'])
@jwt_required()
def update_risk(risk_id):
    """Update a risk"""
    risk = Risk.query.get_or_404(risk_id)
    data = request.get_json()

    old_status = risk.status

    allowed_fields = ['title', 'description', 'category', 'probability', 'impact',
                      'status', 'owner_id', 'mitigation_plan', 'contingency_plan',
                      'response_strategy', 'affected_milestones', 'affected_tasks']

    for field in allowed_fields:
        if field in data:
            setattr(risk, field, data[field])

    if 'target_resolution_date' in data:
        risk.target_resolution_date = datetime.fromisoformat(data['target_resolution_date']).date() if data['target_resolution_date'] else None
    if 'actual_resolution_date' in data:
        risk.actual_resolution_date = datetime.fromisoformat(data['actual_resolution_date']).date() if data['actual_resolution_date'] else None

    # Recalculate risk score if probability or impact changed
    if 'probability' in data or 'impact' in data:
        risk.calculate_risk_score()

    # If resolved, set resolution date
    if data.get('status') in ['resolved', 'closed'] and old_status not in ['resolved', 'closed']:
        risk.actual_resolution_date = datetime.utcnow().date()

    db.session.commit()

    # Trigger automations
    from app.services.automation_engine import AutomationEngine
    engine = AutomationEngine()
    if data.get('status') and data['status'] != old_status:
        engine.trigger('risk_status_changed', risk, changes={
            'old_status': old_status,
            'new_status': data['status']
        })

    return jsonify(risk.to_dict()), 200


@risks_bp.route('/<int:risk_id>', methods=['DELETE'])
@jwt_required()
def delete_risk(risk_id):
    """Delete a risk"""
    risk = Risk.query.get_or_404(risk_id)
    db.session.delete(risk)
    db.session.commit()
    return jsonify({'message': 'Risk deleted'}), 200


# Risk matrix/heatmap
@risks_bp.route('/matrix', methods=['GET'])
@jwt_required()
def get_risk_matrix():
    """Get risk matrix data for heatmap visualization"""
    project_id = request.args.get('project_id', type=int)

    query = Risk.query.filter(Risk.status.notin_(['resolved', 'closed']))
    if project_id:
        query = query.filter_by(project_id=project_id)

    risks = query.all()

    # Build matrix
    matrix = {}
    for prob in ['very_low', 'low', 'medium', 'high', 'very_high']:
        matrix[prob] = {}
        for imp in ['very_low', 'low', 'medium', 'high', 'very_high']:
            matrix[prob][imp] = []

    for risk in risks:
        matrix[risk.probability][risk.impact].append({
            'id': risk.id,
            'title': risk.title,
            'score': risk.risk_score
        })

    return jsonify({
        'matrix': matrix,
        'total_risks': len(risks)
    }), 200


# Issues endpoints
@risks_bp.route('/issues', methods=['GET'])
@jwt_required()
def get_issues():
    """Get all issues"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    project_id = request.args.get('project_id', type=int)
    status = request.args.get('status')

    query = Issue.query

    if project_id:
        query = query.filter_by(project_id=project_id)
    if status:
        query = query.filter_by(status=status)

    pagination = query.order_by(Issue.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'issues': [i.to_dict() for i in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@risks_bp.route('/issues', methods=['POST'])
@jwt_required()
def create_issue():
    """Create a new issue"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('project_id'):
        return jsonify({'error': 'project_id is required'}), 400
    if not data.get('title'):
        return jsonify({'error': 'Issue title is required'}), 400

    issue = Issue(
        project_id=data['project_id'],
        title=data['title'],
        description=data.get('description'),
        category=data.get('category'),
        severity=data.get('severity', 'medium'),
        priority=data.get('priority', 'medium'),
        status=data.get('status', 'open'),
        owner_id=data.get('owner_id', user_id),
        assigned_to_id=data.get('assigned_to_id'),
        related_risk_id=data.get('related_risk_id')
    )

    if data.get('target_resolution_date'):
        issue.target_resolution_date = datetime.fromisoformat(data['target_resolution_date']).date()

    db.session.add(issue)
    db.session.commit()

    return jsonify(issue.to_dict()), 201


@risks_bp.route('/issues/<int:issue_id>', methods=['PUT'])
@jwt_required()
def update_issue(issue_id):
    """Update an issue"""
    issue = Issue.query.get_or_404(issue_id)
    data = request.get_json()

    allowed_fields = ['title', 'description', 'category', 'severity', 'priority',
                      'status', 'owner_id', 'assigned_to_id', 'resolution', 'root_cause']

    for field in allowed_fields:
        if field in data:
            setattr(issue, field, data[field])

    if 'target_resolution_date' in data:
        issue.target_resolution_date = datetime.fromisoformat(data['target_resolution_date']).date() if data['target_resolution_date'] else None
    if 'actual_resolution_date' in data:
        issue.actual_resolution_date = datetime.fromisoformat(data['actual_resolution_date']).date() if data['actual_resolution_date'] else None

    db.session.commit()
    return jsonify(issue.to_dict()), 200
