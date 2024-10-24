from marshmallow import validates, ValidationError
from app.extensions import ma

class ProductSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'farm_id', 'name', 'crop_type', 'quantity', 'unit',
            'price_per_unit', 'quality_grade', 'harvest_date', 'description',
            'images', 'available', 'created_at'
        )
    
    @validates('quantity')
    def validate_quantity(self, value):
        if value <= 0:
            raise ValidationError("Quantity must be greater than 0")

    @validates('price_per_unit')
    def validate_price(self, value):
        if value <= 0:
            raise ValidationError("Price must be greater than 0")