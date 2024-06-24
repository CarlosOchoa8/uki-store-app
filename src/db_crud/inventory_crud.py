"""
Generate an Object of CRUD
"""
from typing import Any, List

from sqlalchemy.exc import SQLAlchemyError

from database.crud_base import CRUDBase
from sqlalchemy.orm import lazyload, load_only, subqueryload, Load, joinedload
from database.db import db
from forms import InventoryCreateForm, InventoryUpdateForm
from models import Inventory as InventoryModel
from models import Product as ProductModel

class CRUDInventory(CRUDBase[InventoryModel, InventoryCreateForm, InventoryUpdateForm]):
    """User CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """

    def get_multi(self, page: int | None = 1, per_page: int = 18) -> List[InventoryModel]:
        return self.model.query.options(
            joinedload(InventoryModel.product).
            load_only(ProductModel.name, ProductModel.sku, ProductModel.price)
            ).paginate(page=page, per_page=per_page, error_out=False)


inventory_crud = CRUDInventory(InventoryModel)
