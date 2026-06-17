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
Every call of `flag` or `key` generates 2-character key. This key is represented as left and right indexes of `f"{ascii_letters}{digits}"` str. Each time the left index reaches cap, it resets to 0 and right index increments.<br>
After reaching both of caps, next call of function will throw `OverflowError`. Current maximum count of keys is 3844.

#### Typing
`key` function requires `value_type` argument, such as `str`, `int` etc. This type used in both static analysis and type convertion with `Key.parse_entry(data)` function. 

## Examples
Main purpose of this library is making telegram bot's "callback_data" much more compact because of 64-byte limit. You can see more realistic example [here](example)<br><br>
#### Flag usage
Before:
```python
from enum import StrEnum, auto()

# Some very strict limit
MAX_LEN: int = 4

class Status(StrEnum):
    PENDING = auto()
    APPROVED = auto()
    REJECTED = auto()

assert Status.PENDING == "pending"
assert len(Status.PENDING) > MAX_LEN  # Too long! 
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
    USER = auto()
    ORDER = auto()

username = Data.USER + name

```
```python
from microconst import key, parse_entry

class Data:
    USER = key(str)
    ORDER = key(int)

# You can call keys to create key-value pair (acts same as concat)
username = Data.USER("name") 
assert username == "aaname"

# Getting value
value = Data.USER.parse_entry(username) 
assert value == "name"

order = Data.ORDER(1337)
assert order == "ba1337"

# You can use seperate function or method. Method doesnt require type argument
assert parse_entry(order, int) == 1337
assert Data.ORDER.parse_entry(order) == 1337

```

## License
MIT
