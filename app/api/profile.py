from flask import Blueprint, request, jsonify
from flask_security import auth_required, current_user
from app.models.farm import Farm
from app.extensions import db

profile_bp = Blueprint('profile', __name__, url_prefix='/api/profile')

@profile_bp.route('/farm', methods=['POST'])
@auth_required()
def create_farm():
    data = request.get_json()
    
    farm = Farm(
        user_id=current_user.id,
        name=data['name'],
        location=data['location'],
        size=data['size'],
        farming_methods=data['farming_methods']
    )
    
    db.session.add(farm)
    db.session.commit()
    
    return jsonify({'message': 'Farm profile created successfully'}), 201

@profile_bp.route('/farm', methods=['GET'])
@auth_required()
def get_farm():
    # Get farm profile code
    pass