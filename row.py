from typing import Any

from utility import validate_item_class
from data_type import DataType


class Row:
    # Attributes
    content: list
    primary_key_index: int


    # Contructor
    def __init__(self, primary_key_index: int) -> None:
        # validate parameters
        validate_item_class(primary_key_index, int)

        # assign attribute values
        self.content = []
        self.primary_key_index = primary_key_index


    # Methods
    def set(self, index: int, value: Any = None) -> None:
        # validate parameters
        validate_item_class(index, int)

        # check if the index is being set to its default value
        if value is None:
            # set index to its default value
            self.content[index] = DataType.get_default_value(self.content[index])

        else:
            # set index to value
            self.content[index] = value

    def get(self, index: int) -> Any:
        # validate parameters
        validate_item_class(index, int)

        # return the value at index
        return self.content[index]