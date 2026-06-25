# microconst
[![pypi](https://img.shields.io/pypi/v/microconst)](https://pypi.org/project/microconst/)
![python](https://img.shields.io/badge/python-3.12+-blue?logo=python)
![typed](https://img.shields.io/badge/typed-yes-blue)
![tests](https://img.shields.io/badge/tests-manual-green) 
![license](https://img.shields.io/badge/license-MIT-blue)

Replace long constant names with 2 ASCII characters

## Installation
pip: 
```
pip install microconst
```
poetry:
```
poetry add microconst
```

## Features
#### Constants
Every call of `flag` or `key` generates 2-character constant. This constant is represented as left and right indexes of `f"{ascii_letters}{digits}"` str. Each time the left index reaches cap, it resets to 0 and right index increments.<br>
After reaching both of caps, next call of function will throw `OverflowError`. Current maximum count of constants is 3844.

#### Typing
`key` function requires `value_type` argument, such as `str`, `int` etc. This type used in both static analysis and type conversion with `Key.parse_entry` function. 

## Examples
Main purpose of this library is making telegram bot's "callback_data" much more compact because of 64-byte limit. You can see more realistic example [here](example)<br>
#### Flag usage
Before:
```python
from enum import StrEnum, auto

# Some very strict limit
MAX_LEN: int = 4

class Status(StrEnum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()

assert Status.PENDING == "pending"
assert len(Status.PENDING) > MAX_LEN  # Too long
```
After:
```python
from microconst import flag

MAX_LEN: int = 4

# Autogenerates unique pairs of characters
class Status:
    PENDING = flag()
    APPROVED = flag()
    REJECTED = flag()

assert Status.PENDING == "aa"
assert len(Status.PENDING) < MAX_LEN 
```

#### Key usage
Before:
```python
from enum import StrEnum, auto

class Data(StrEnum):
    USERNAME = auto()
    ORDER = auto()

# You should use separator because of varying character count in key
username = Data.USERNAME + ":" + "name"
assert username == "username:name"  # Too long

value = username.split(":")[1]
assert value == "name"

order = Data.ORDER + ":" + str(1337)
assert order == "order:1337"

# Order doesnt contain its type anywhere, so you should convert types each time
assert int(order.split(":")[1]) == 1337

```
After:
```python
from microconst import key, parse_entry

class Data:
    USERNAME = key(str)
    ORDER = key(int)

# You can call keys to create key-value pair (acts same as concat)
username = Data.USERNAME("name")
assert username == "aaname"

# Getting value
value = Data.USERNAME.parse_entry(username)
assert value == "name"

order = Data.ORDER(1337)
assert order == "ba1337"

# You can use separate function or method. Method doesnt require type argument
assert parse_entry(order, int) == 1337
assert Data.ORDER.parse_entry(order) == 1337
```

#### Key usage (literals)
Unique feature, it's hard to implement, so no comprasion before and after:
```python
from microconst import key, parse_entry

class Data:
    ORDER = key(Literal[1, 2, 3])

assert Data.ORDER(1) == "aa1"
# assert Data.ORDER(4) == "aa4"  # Mypy error

assert Data.ORDER.parse_entry("__3") == 3
# assert Data.ORDER.parse_entry("__10") == 10  # Mypy error
```

## License
MIT
