"""
Portfolios API endpoints
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Portfolio, User

portfolios_bp = Blueprint('portfolios', __name__)


@portfolios_bp.route('', methods=['GET'])
@jwt_required()
def get_portfolios():
    """Get all portfolios"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    status = request.args.get('status')

    query = Portfolio.query

    if status:
        query = query.filter_by(status=status)

    pagination = query.order_by(Portfolio.created_at.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )

    return jsonify({
        'portfolios': [p.to_dict() for p in pagination.items],
        'total': pagination.total,
        'pages': pagination.pages,
        'current_page': page
    }), 200


@portfolios_bp.route('', methods=['POST'])
@jwt_required()
def create_portfolio():
    """Create a new portfolio"""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get('name'):
        return jsonify({'error': 'Portfolio name is required'}), 400

    portfolio = Portfolio(
        name=data['name'],
        description=data.get('description'),
        owner_id=data.get('owner_id', user_id),
        status=data.get('status', 'active'),
        color=data.get('color', '#6366F1'),
        total_budget=data.get('total_budget', 0.0),
        currency=data.get('currency', 'USD')
    )
    db.session.add(portfolio)
    db.session.commit()

    return jsonify(portfolio.to_dict()), 201


@portfolios_bp.route('/<int:portfolio_id>', methods=['GET'])
@jwt_required()
def get_portfolio(portfolio_id):
    """Get a specific portfolio"""
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    include_programs = request.args.get('include_programs', 'false').lower() == 'true'
    return jsonify(portfolio.to_dict(include_programs=include_programs)), 200


@portfolios_bp.route('/<int:portfolio_id>', methods=['PUT'])
@jwt_required()
def update_portfolio(portfolio_id):
    """Update a portfolio"""
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    data = request.get_json()

    allowed_fields = ['name', 'description', 'owner_id', 'status',
                      'color', 'total_budget', 'currency']

    for field in allowed_fields:
        if field in data:
            setattr(portfolio, field, data[field])

    db.session.commit()
    return jsonify(portfolio.to_dict()), 200


@portfolios_bp.route('/<int:portfolio_id>', methods=['DELETE'])
@jwt_required()
def delete_portfolio(portfolio_id):
    """Delete a portfolio"""
    portfolio = Portfolio.query.get_or_404(portfolio_id)

    # Check if has programs
    if portfolio.programs.count() > 0:
        return jsonify({'error': 'Cannot delete portfolio with programs'}), 400

    db.session.delete(portfolio)
    db.session.commit()
    return jsonify({'message': 'Portfolio deleted'}), 200


@portfolios_bp.route('/<int:portfolio_id>/dashboard', methods=['GET'])
@jwt_required()
def get_portfolio_dashboard(portfolio_id):
    """Get portfolio dashboard statistics"""
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    stats = portfolio.get_dashboard_stats()

    # Get program details
    programs_data = []
    for program in portfolio.programs:
        programs_data.append({
            'id': program.id,
            'name': program.name,
            'status': program.status,
            'progress': program.get_progress(),
            'project_count': program.projects.count(),
            'budget': program.budget,
            'actual_cost': program.actual_cost
        })

    stats['programs'] = programs_data
    stats['portfolio'] = portfolio.to_dict()

    return jsonify(stats), 200
