"""
Generate an Object of CRUD
"""
from typing import Any

from sqlalchemy.exc import SQLAlchemyError

from database.crud_base import CRUDBase
from database.db import db
from forms import UserCreateForm, UserUpdateForm
from models import Address as AddressModel


class CRUDAddress(CRUDBase[AddressModel, UserCreateForm, UserUpdateForm]):
    """User CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """


address_crud = CRUDAddress(AddressModel)
