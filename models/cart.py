from typing import List
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_id: Mapped[int] = mapped_column(db.ForeignKey('customers.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.ForeignKey('product.id'), nullable=False)

    customer: Mapped['Customer'] = relationship('Customer', back_populates='carts')
    product: Mapped['Product'] = relationship('Product', back_populates='carts')


