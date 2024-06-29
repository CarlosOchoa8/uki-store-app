from sqlalchemy.orm import relationship

from database.db import db


class Product(db.Model):
    """ Class for Product db presentation. """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    label = db.Column(db.String, nullable=True)
    description = db.Column(db.Text, nullable=True)
    sku = db.Column(db.String, nullable=True)
    main_picture = db.Column(db.Text, nullable=False)
    available = db.Column(db.Boolean, nullable=False)

    inventory = relationship("Inventory", back_populates="product")
    # def __init__(self, name, category, price, main_picture):
    #     self.name = name
    #     self.category = category
    #     self.price = price
    #     self.main_picture = main_picture

    def __repr__(self):
        return (f"<{self.id}>"
                f"<{self.name}>"
                f"<{self.category}>"
                f"<{self.price}>")

    @property
    def formatted_price(self):
        """ Return the formatted price of the product. """
        return f"{self.price:,.2f} COP."
