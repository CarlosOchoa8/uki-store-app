from database.db import db
from utils.inventory_stock_custom_type import InventoryStatusType


class Inventory(db.Model):
    """Address db model class."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    product_stock = db.Column(InventoryStatusType, nullable=False)

    def __repr__(self):
        return (f"<{self.product_id}>"
                f"<{self.product_stock}>"
                )
