from flask import Blueprint
from controllers.cartController import add_to_cart, remove_from_cart, view_cart, empty_cart

cart_bp = Blueprint('cart', __name__)

cart_bp.route('/cart', methods=['POST'])(add_to_cart)
cart_bp.route('/cart/remove', methods=['POST'])(remove_from_cart)
cart_bp.route('/cart/<int:customer_id>', methods=['GET'])(view_cart)
cart_bp.route('/cart/empty/<int:customer_id>', methods=['DELETE'])(empty_cart)
