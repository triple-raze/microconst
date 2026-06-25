from __future__ import annotations

from collections.abc import Callable
from typing import Literal, Self, cast, get_args, get_origin, overload

from typing_extensions import TypeForm

from microconst.utils import parse_entry

# Any type is callable, but mypy doesnt think so
# It also means you can use functions instead of types technically
type Converter[T] = Callable[[str], T]


class Key[T](str):
    # Subclasses of str should define __slots__
    __slots__ = ("converter",)
    converter: Converter[T]

    @overload
    def __new__(cls, name: str, converter: Converter[T], /) -> Key[T]: ...

    @overload
    def __new__(cls, name: str, literal: TypeForm[T], /) -> Key[T]: ...

    def __new__(cls, name: str, converter_or_literal: object) -> Key[T]:
        instance = super().__new__(cls, name)

        # Type forms has __call__, but it throws an exception. We will use isinstance with type insead
        is_converter = isinstance(converter_or_literal, type(object))

        origin = cast("object", get_origin(converter_or_literal))

        if not is_converter and origin is not Literal:
            msg = f"Callable or literal excepted, got {type(converter_or_literal)}"
            raise TypeError(msg)

        if is_converter:
            instance.converter = cast("Converter[T]", converter_or_literal)
            return instance

        literal_values = cast("tuple[object, ...]", get_args(converter_or_literal))

        for value in literal_values:
            if type(value) is not type(literal_values[0]):
                msg = (
                    "Literal should have items of only one type. "
                    f"Excepted {type(literal_values[0])}, found {type(value)}"
                )
                raise TypeError(msg)

        instance.converter = cast("Converter[T]", type(literal_values[0]))

        return instance

    def __call__(self, value: T) -> Entry[T]:
        return Entry(self.__str__(), value)

    def parse_entry(self, entry: Entry[T] | str) -> T:
        return parse_entry(entry, self.converter)


class Entry[T](str):
    __slots__ = ("key", "value")
    key: str
    value: T

    def __new__(cls, key: str, value: T) -> Self:
        instance = super().__new__(cls, f"{key}{value}")
        instance.key = key
        instance.value = value
        return instance
