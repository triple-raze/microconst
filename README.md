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
#### Flag usage:
```python
from microconst import flag

# Autogenerates unique pairs of characters
class Status:
    PENDING = flag()
    APPROVED = flag()
    REJECTED = flag()

assert Status.PENDING == "aa"
assert Status.APPROVED == "ba"
assert Status.REJECTED == "ca"
```

#### Key usage:
```python
from microconst import key, parse_entry

USER = key(str)

# You can call keys to create key-value pair (acts same as concat)
username = USER("name") 
# Getting value
value = USER.parse_entry(username) 

assert username == "aaname"
assert value == "name"

# You can use seperate function or method. Method doesnt require type argument
assert parse_entry(username, str) == value
```

## License
MIT
