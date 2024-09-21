from flask import request, jsonify
from models.schemas.cartSchema import cart_schema, carts_schema
from services import cartService
from marshmallow import ValidationError
from cache import cache
from database import db


cart_service = CartService()

def add_to_cart():
    data = request.get_json()
    customer_id = data.get('customer_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    cart_item = cart_service.add_item(customer_id, product_id, quantity)
    return jsonify(cart_item), 201

def remove_from_cart():
    data = request.get_json()
    customer_id = data.get('customer_id')
    product_id = data.get('product_id')

    cart_service.remove_item(customer_id, product_id)
    return jsonify({"message": "Item removed from cart"}), 200

def view_cart(customer_id):
    cart_items = cart_service.view_cart(customer_id)
    return jsonify(cart_items), 200


def empty_cart():
    current_user_id = get_jwt_identity()
    Cart.query.filter_by(customer_id=current_user_id).delete()
    db.session.commit()
    return jsonify({"message": "Cart emptied"}), 200

