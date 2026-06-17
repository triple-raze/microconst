from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from microconst.types import ConverterType


def parse_entry[T](data: str, value_type: ConverterType[T]) -> T:
    str_value = data[2:]
    return value_type(str_value)
