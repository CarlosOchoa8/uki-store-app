"""
Generate an Object of CRUD
"""
from typing import Any

from sqlalchemy import insert
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from database.crud_base import CRUDBase
from database.db import db
from forms import ProductCreateForm, ProductUpdateForm
from models import Product, ProductImage, Inventory
from services.save_files import save_files_to_static
from utils.inventory_constants import InventoryStock

class CRUDProduct(CRUDBase[Product, ProductCreateForm, ProductUpdateForm]):
    """Product CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def create(self, obj_in: list[ProductCreateForm] | dict[str, Any]) -> Product:
        """Create Product model object and insert its images in model ProductImage."""
        try:
            inventory_stock = obj_in["product_stock"]
            obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.dict()
            product_files = save_files_to_static(
                category=obj_in["category"],
                upload_files=obj_in["main_picture"]
                )
            obj_in_data["main_picture"] = product_files[0]
            db_obj = self.model(
                **{f: v for f, v in obj_in_data.items() if hasattr(self.model, f)}
                )
            db.session.add(db_obj)
            db.session.flush()

            products_images = [
                {"file_name": file, "product_id": db_obj.id}
                for file in product_files
                ]
            bulk_files_insert = insert(ProductImage).values(products_images)

            inv_stock = Inventory(
                product_id= db_obj.id,
                product_stock= InventoryStock(inventory_stock)
            )

            db.session.add(inv_stock)
            db.session.execute(bulk_files_insert)
            db.session.commit()
            db.session.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            db.session.rollback()
            raise SQLAlchemyError(f"Error: {str(e)}") from e

    def get(self, id: int) -> Product:
        return self.model.query.filter(self.model.id == id).options(joinedload(self.model.inventory)).first()

    def filter_by_category(self, param: str, page: int | None = 1, per_page: int = 18) -> list[Product]:
        """Return items by specific category"""
        return self.model.query.filter(
            self.model.category == param).paginate(
                page=page, per_page=per_page, error_out=False)


    def get_products_categories(self) -> list[Product]:
        """Return a list with all products categories."""
        return [category[0] for category in
                self.model.query.with_entities(self.model.category).distinct().all()
                ]

product_crud = CRUDProduct(Product)
