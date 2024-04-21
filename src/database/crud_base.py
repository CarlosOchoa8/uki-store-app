from sqlalchemy.exc import SQLAlchemyError
from typing import Type, Generic, TypeVar, Any, List
from flask_sqlalchemy.pagination import Pagination
from .db import db

ModelType = TypeVar('ModelType')
CreateFormType = TypeVar('CreateFormType')
UpdateFormType = TypeVar('UpdateFormType')


class CRUDBase(Generic[ModelType, CreateFormType, UpdateFormType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        Args:
        `model`: A SQLAlchemy model class
        """
        self.model = model

    def create(self, obj_in: CreateFormType | dict[str, Any]) -> ModelType:
        """Create a ModelType object"""
        try:
            obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.dict()
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

    def update(self, obj_in: UpdateFormType | dict[str, Any], db_obj: ModelType) -> ModelType:
        """Update a Model object"""
        try:
            obj_in_data = obj_in if isinstance(obj_in, dict) else obj_in.dict(exclude_none=True)
            for field in obj_in_data:
                if hasattr(db_obj, field):
                    setattr(db_obj, field, obj_in_data[field])
            db.session.add(db_obj)
            db.session.commit()
            return db_obj
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    def get(self, id: int) -> ModelType:
        """Get a single Model filtered by id"""
        return self.model.query.get(id)

    def get_multi(self, page: int | None = 1, per_page: int = 18) -> List[ModelType]:
        """Get all Model objects paginated"""
        return self.model.query.paginate(page=page, per_page=per_page, error_out=False)
