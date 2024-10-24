from app.extensions import db
from datetime import datetime

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    size = db.Column(db.Float)
    farming_methods = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    products = db.relationship('Product', backref='farm', lazy='dynamic')