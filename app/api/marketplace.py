from flask_security import auth_required, current_user
from flask import Blueprint, request, jsonify
from datetime import datetime
from app.extensions import db
from app.models.product import Product
from app.schemas.product_schema import ProductSchema


marketplace_bp = Blueprint('marketplace', __name__, url_prefix='/api/marketplace')

@marketplace_bp.route('/products', methods=['POST'])
@auth_required()
def create_product():
    data = request.get_json()
    
    product = Product(
        farm_id=current_user.farm.id,
        name=data['name'],
        crop_type=data['crop_type'],
        quantity=data['quantity'],
        unit=data['unit'],
        price_per_unit=data['price_per_unit'],
        quality_grade=data['quality_grade'],
        harvest_date=datetime.strptime(data['harvest_date'], '%Y-%m-%d'),
        description=data['description'],
        images=data['images']
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify({'message': 'Product created successfully'}), 201

@marketplace_bp.route('/products', methods=['GET'])
def list_products():
    products = Product.query.filter_by(available=True).all()
    schema = ProductSchema(many=True)
    return jsonify(schema.dump(products))