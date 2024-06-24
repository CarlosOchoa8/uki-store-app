from database.db import db
from utils.inventory_stock_custom_type import InventoryStatusType
from sqlalchemy.orm import relationship

class Inventory(db.Model):
    """Address db model class."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    product_stock = db.Column(InventoryStatusType, nullable=False)
    product = relationship("Product", back_populates="inventory")

    def __repr__(self):
        return (f"<{self.product_id}>"
                f"<{self.product_stock}>"
                )
