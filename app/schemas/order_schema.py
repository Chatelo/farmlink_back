import marshmallow as ma
from marshmallow.validate import validates, ValidationError

class OrderSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'buyer_id', 'product_id', 'quantity', 'total_price',
            'status', 'created_at', 'payment_id'
        )
    
    @validates('quantity')
    def validate_quantity(self, value):
        if value <= 0:
            raise ValidationError("Quantity must be greater than 0")

    @validates('status')
    def validate_status(self, value):
        valid_statuses = ['pending', 'paid', 'shipped', 'delivered', 'cancelled']
        if value not in valid_statuses:
            raise ValidationError("Invalid order status")

class PaymentSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'order_id', 'amount', 'status', 'payment_method',
            'transaction_id', 'created_at'
        )
    
    @validates('amount')
    def validate_amount(self, value):
        if value <= 0:
            raise ValidationError("Amount must be greater than 0")

    @validates('status')
    def validate_status(self, value):
        valid_statuses = ['pending', 'completed', 'failed', 'refunded']
        if value not in valid_statuses:
            raise ValidationError("Invalid payment status")

    @validates('payment_method')
    def validate_payment_method(self, value):
        valid_methods = ['credit_card', 'bank_transfer', 'mobile_money']
        if value not in valid_methods:
            raise ValidationError("Invalid payment method")