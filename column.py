from data_type import DataType
from utility import validate_item_class


class Column:
    # Attributes
    id: str
    data_type: DataType
    is_primary_key: bool


    # Constructor
    def __init__(self, id: str, data_type: DataType, is_primary_key: bool) -> None:
        # validate parameters
        validate_item_class(id, str)
        validate_item_class(data_type, DataType)
        validate_item_class(is_primary_key, bool)

        # assign attribute values
        self.id = id
        self.data_type = data_type
        self.is_primary_key = is_primary_key