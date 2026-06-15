from collections.abc import Callable
from typing import Self

from microconst.entry import parse_entry
from microconst.key import unique_key_generator


class Key[T](str):
    # Subclasses of str should define __slots__
    __slots__ = ("type",)
    # We'll assign to this in __new__
    type: Callable[[str], T]

    def __new__(cls, name: str, value_type: Callable[[str], T]) -> Self:
        instance = super().__new__(cls, name)
        instance.type = value_type
        return instance

    def __call__(self, value: T) -> str:
        return f"{self}{value}"

    def parse_entry(self, data: str) -> T:
        return parse_entry(data, self.type)


def create_flag() -> str:
    return next(unique_key_generator)


def create_key[T](value_type: type[T]) -> Key[T]:
    name = next(unique_key_generator)
    return Key(name, value_type)
