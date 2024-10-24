from flask import Blueprint, request, jsonify
from flask_security import auth_required, current_user
from app.models.order import Order
from app.models.product import Product
from app.extensions import db

payment_bp = Blueprint('payment', __name__, url_prefix='/api/payment')

@payment_bp.route('/orders', methods=['POST'])
@auth_required()
def create_order():
    data = request.get_json()
    product = Product.query.get_or_404(data['product_id'])
    
    if product.quantity < data['quantity']:
        return jsonify({'error': 'Insufficient quantity available'}), 400
        
    order = Order(
        buyer_id=current_user.id,
        product_id=product.id,
        quantity=data['quantity'],
        total_price=product.price_per_unit * data['quantity'],
        status='pending'
    )
    
    db.session.add(order)
    db.session.commit()
    
    return jsonify({'message': 'Order created successfully'}), 201

@payment_bp.route('/orders/<int:order_id>', methods=['GET'])
@auth_required()
def get_order(order_id):
    # Get specific order code
    pass