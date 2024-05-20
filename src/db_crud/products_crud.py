"""
Generate an Object of CRUD
"""
from typing import Any
from database.crud_base import CRUDBase
from database.db import db
from forms import ProductCreateForm, ProductUpdateForm
from models import Product
from sqlalchemy.exc import SQLAlchemyError
from services.save_files import save_files_to_static 


class CRUDCourse(CRUDBase[Product, ProductCreateForm, ProductUpdateForm]):
    """Product CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def create(self, obj_in: ProductCreateForm | dict[str, Any]) -> Product:
        try:
            obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.dict()
            obj_in_data["main_picture"] = save_files_to_static(category=obj_in["category"] ,upload_file=obj_in["main_picture"])
            db_obj = self.model(
                **{f: v for f, v in obj_in_data.items() if hasattr(self.model, f)}
                )
            
            db.session.add(db_obj)
            db.session.commit()
            db.session.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            db.session.rollback()
            raise SQLAlchemyError(f"Error: {str(e)}")

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

product_crud = CRUDCourse(Product)
