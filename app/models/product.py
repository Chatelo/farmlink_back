from app.extensions import db
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'))
    name = db.Column(db.String(255))
    crop_type = db.Column(db.String(100))
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(50))
    price_per_unit = db.Column(db.Float)
    quality_grade = db.Column(db.String(50))
    harvest_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    images = db.Column(db.JSON)
    available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)