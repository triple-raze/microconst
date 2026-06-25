from typing import Literal

from microconst import flag, key, parse_entry


def test_member_creation() -> None:
    assert key(int)(10) == "aa10"

    assert key(str)("hello") == "bahello"

    assert key(float)(14.1) == "ca14.1"

    assert flag() == "da"
    assert flag() == "ea"


def test_value_extraction() -> None:
    int_k = key(int)
    data = int_k(123)

    assert int_k.parse_entry(data) == 123

    assert data.value == 123

    assert parse_entry("__1.2", float) == 1.2


def test_literal_key() -> None:
    int_k = key(Literal[1, 2, 3])
    assert int_k(3)

    str_k = key(Literal["hi", "hello", "greetings"])
    assert str_k.parse_entry("__hi") == "hi"
