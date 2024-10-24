from flask import Flask
from config import Config
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Debug print to verify loaded config
    print("SECRET_KEY:", app.config['SECRET_KEY'])
    print("DATABASE_URL:", app.config['SQLALCHEMY_DATABASE_URI'])
    
    db.init_app(app)

    return app
