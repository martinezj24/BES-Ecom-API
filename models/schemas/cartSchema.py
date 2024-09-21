from . import ma
from models.cart import Cart
from marshmallow import fields

class CartSchema(Schema):
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)

    class Meta:
        model = Cart
        load_instance = True  # Automatically create instance of the Cart model

cart_schema = CartSchema()
carts_schema = CartSchema(many=True)
