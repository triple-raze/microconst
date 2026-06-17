from microconst import flag, key, parse_entry


def test_member_creation() -> None:
    assert key(int)(10) == "aa10"

    assert key(str)("hello") == "bahello"

    assert key(float)(14.1) == "ca14.1"

    assert flag() == "da"
    assert flag() == "ea"


def test_value_extraction() -> None:
    int_key = key(int)
    data = int_key(123)

    assert int_key.parse_entry(data) == 123

    assert data.value == 123

    assert parse_entry("aa1.2", float) == 1.2
