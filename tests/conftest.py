import pytest
import sys
from pathlib import Path

# Add the project root directory to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app import create_app
from app.extensions import db
from app.models.user import User, Role

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'postgresql://localhost/farmapp_test',
        'WTF_CSRF_ENABLED': False
    })
    
    with app.app_context():
        db.create_all()
        # Create test roles
        farmer_role = Role(name='farmer', description='Farmer role')
        buyer_role = Role(name='buyer', description='Buyer role')
        db.session.add(farmer_role)
        db.session.add(buyer_role)
        db.session.commit()
        
        yield app
        
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def farmer(app):
    with app.app_context():
        user = User(
            email='farmer@example.com',
            phone='+1234567890',
            password='SecurePass123!',
            active=True
        )
        farmer_role = Role.query.filter_by(name='farmer').first()
        user.roles.append(farmer_role)
        db.session.add(user)
        db.session.commit()
        return user