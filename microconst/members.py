from __future__ import annotations

from typing import TYPE_CHECKING

from microconst.const import unique_const_generator
from microconst.types import Key

if TYPE_CHECKING:
    from microconst.types import ConverterType


def create_flag() -> str:
    return next(unique_const_generator)


def create_key[T](value_type: ConverterType[T]) -> Key[T]:
    name = next(unique_const_generator)
    return Key(name, value_type)
