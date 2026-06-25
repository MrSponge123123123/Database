from enum import Enum
from typing import Any


class DataType(Enum):
    String = str
    Int = int
    Float = float
    Bool = bool

    @classmethod
    def get_data_type(cls, value: Any) -> DataType:
        # check if value is a DataType, type or value
        if type(value) == DataType:
            return value

        elif type(value) == type:
            # Return DataType of value if it is a type (class)
            if value == str: return DataType.String
            elif value == int: return DataType.Int
            elif value == float: return DataType.Float
            elif value == bool: return DataType.Bool

        else:
            # Return DataType of value if it is a value
            if type(value) == str: return DataType.String
            elif type(value) == int: return DataType.Int
            elif type(value) == float: return DataType.Float
            elif type(value) == bool: return DataType.Bool

        raise ValueError(f"{value} is not part of any DataType")

    @classmethod
    def get_default_value(cls, value: Any) -> Any:
        # get the DataType of value
        data_type: DataType = cls.get_data_type(value)

        if data_type == DataType.String: return ""
        elif data_type == DataType.Int: return 0
        elif data_type == DataType.Float: return 0.0
        elif data_type == DataType.Bool: return False
        raise ValueError(f"{value} is not part of any DataType")