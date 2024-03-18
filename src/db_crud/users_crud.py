"""
Generate an Object of CRUD
"""
from typing import Any

from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash

from database.crud_base import CRUDBase
from database.db import db
from forms import UserCreateForm, UserUpdateForm
from models import User


class CRUDCourse(CRUDBase[User, UserCreateForm, UserUpdateForm]):
    """User CRUD class
    Args:
        CRUDBase ([Item, ItemCreate, ItemUpdate])
    """
    def create(self, obj_in: UserCreateForm | dict[str, Any]) -> User:
        try:
            obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.dict()
            obj_in_data["password"] = generate_password_hash(obj_in_data["password"])
            db_obj = self.model(**obj_in_data)
            db.session.add(db_obj)
            db.session.commit()
            db.session.refresh(db_obj)
            return db_obj
        except SQLAlchemyError as e:
            db.session.rollback()
            raise SQLAlchemyError(f"Error: {str(e)}")


user_crud = CRUDCourse(User)
