from database import db
from models.schemas.cartSchema import cart_schema, carts_schema
from sqlalchemy import select

def add_item(self, customer_id, product_id, quantity):
    cart_item = Cart.query.filter_by(customer_id=customer_id, product_id=product_id).first()

    if cart_item:
        # Update quantity if the item is already in the cart
        cart_item.quantity += quantity
    else:
        # Add a new item to the cart
        cart_item = Cart(customer_id=customer_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return cart_schema.dump(cart_item)

def remove_item(self, customer_id, product_id):
    cart_item = Cart.query.filter_by(customer_id=customer_id, product_id=product_id).first()
        
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()

def view_cart(self, customer_id):
    cart_items = Cart.query.filter_by(customer_id=customer_id).all()
    return carts_schema.dump(cart_items)

def empty_cart(self, customer_id):
    Cart.query.filter_by(customer_id=customer_id).delete()
    db.session.commit()