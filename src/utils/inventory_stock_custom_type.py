from sqlalchemy import TypeDecorator, String
from utils.inventory_constants import InventoryStock


class InventoryStatusType(TypeDecorator):
    impl = String

    def process_bind_param(self, value, dialect):
        if isinstance(value, InventoryStock):
            return value.value
        return value

    def process_result_value(self, value, dialect):
        try:
            return InventoryStock(value)
        except ValueError:
            return value
