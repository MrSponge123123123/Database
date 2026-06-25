from typing import Any


def validate_item_class(item: Any, expected_class: type) -> None:
    # validate parameters
    if not isinstance(expected_class, type): raise TypeError(f"Expected: type, got: {type(expected_class)}")

    if not isinstance(item, expected_class): raise TypeError(f"Expected: {expected_class}, got: {type(item)}")