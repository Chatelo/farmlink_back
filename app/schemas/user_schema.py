from marshmallow import validates, ValidationError
from app.utils.validators import validate_phone, validate_password
from app.extensions import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'phone', 'active', 'confirmed_at', 'roles', 'farm')
    
    @validates('phone')
    def validate_phone(self, value):
        is_valid, message = validate_phone(value)
        if not is_valid:
            raise ValidationError(message)

    @validates('password')
    def validate_password(self, value):
        is_valid, message = validate_password(value)
        if not is_valid:
            raise ValidationError(message)

class FarmSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location', 'size', 'farming_methods', 'created_at', 'products')