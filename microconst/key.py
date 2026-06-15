from collections.abc import Generator
from string import ascii_letters, digits

CHARACTERS = f"{ascii_letters}{digits}"

MAX_IDX = len(CHARACTERS) - 1
MAX_KEYS = len(CHARACTERS) ** 2


def create_unique_key_generator() -> Generator[str, None, None]:
    left_idx: int = 0
    right_idx: int = 0

    while right_idx != MAX_IDX + 1:
        pair: str = CHARACTERS[left_idx] + CHARACTERS[right_idx]

        if left_idx == MAX_IDX:
            left_idx = 0
            right_idx += 1
        else:
            left_idx += 1

        yield pair

    msg = f"cannot create more than {MAX_KEYS} keys"
    raise OverflowError(msg)


unique_key_generator = create_unique_key_generator()
