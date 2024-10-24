from flask import Flask
from config import Config, TestConfig
from app.extensions import db, security, migrate, ma, mail 
from app.models.user import User, Role
from app.models.order import Order
from app.models.payment import Payment
from flask_security import SQLAlchemyUserDatastore

 
def create_app(config_name='Config'):
    app = Flask(__name__)
    app.config.from_object('app.Config')
    
    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    
    # Register blueprints
    from app.api import marketplace, profile, payment
    app.register_blueprint(marketplace.marketplace_bp)
    app.register_blueprint(profile.profile_bp)
    app.register_blueprint(payment.payment_bp)
    
    return app
