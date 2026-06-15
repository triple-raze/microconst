from collections.abc import Callable


def parse_entry[T](data: str, value_type: Callable[[str], T]) -> T:
    str_value = data[2:]
    return value_type(str_value)
