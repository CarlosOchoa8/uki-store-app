import re
from enum import Enum


class InventoryStock(Enum):
    """Enum class for representation of stock."""
    AVAILABLE = "Disponible"
    UNAVAILABLE = "Agotado"

    @classmethod
    def _missing_(cls, value):
        if re.match(r"^\d+$", value):
        # if isinstance(value, int):
            obj = object.__new__(cls)
            obj._value_ = value
            obj._name_ = "QUANTITY"
            return obj
