"""Define the ProductFile class for managing product images."""
from database.db import db


class ProductImage(db.Model):
    """Products images"""
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

    def __init__(self, file_name):
        self.name = file_name

    def __repr__(self):
        return f"<{self.id}>"
