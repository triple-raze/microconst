from __future__ import annotations

from typing import TYPE_CHECKING, overload

from typing_extensions import TypeForm

from microconst.const import unique_const_generator
from microconst.types import Key

if TYPE_CHECKING:
    from microconst.types import Converter


def create_flag() -> str:
    return next(unique_const_generator)


@overload
def create_key[T](converterl: Converter[T], /) -> Key[T]: ...


@overload
def create_key[T](literal: TypeForm[T], /) -> Key[T]: ...


def create_key[T](converter_or_literal: Converter[T] | TypeForm[T]) -> Key[T]:
    name = next(unique_const_generator)
    return Key(name, converter_or_literal)
