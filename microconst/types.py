from __future__ import annotations

from collections.abc import Callable
from typing import Self

from microconst.utils import parse_entry

# Any type is callable, but mypy doesnt think so
# It also means you can use functions instead of types technically
type ConverterType[T] = Callable[[str], T]


class Key[T](str):
    # Subclasses of str should define __slots__
    __slots__ = ("type",)
    type: ConverterType[T]

    def __new__(cls, name: str, value_type: ConverterType[T]) -> Self:
        instance = super().__new__(cls, name)
        instance.type = value_type
        return instance

    def __call__(self, value: T) -> Entry[T]:
        return Entry(self.__str__(), value)

    def parse_entry(self, data: str) -> T:
        return parse_entry(data, self.type)


class Entry[T](str):
    __slots__ = ("key", "value")
    key: str
    value: T

    def __new__(cls, key: str, value: T) -> Self:
        instance = super().__new__(cls, f"{key}{value}")
        instance.key = key
        instance.value = value
        return instance
