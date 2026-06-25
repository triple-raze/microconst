from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from microconst.types import Converter


def parse_entry[T](data: str, convert: Converter[T]) -> T:
    str_value = data[2:]
    return convert(str_value)
