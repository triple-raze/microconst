from __future__ import annotations

from string import ascii_letters, digits
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

DEFAULT_CHARACTERS = f"{ascii_letters}{digits}"

MAX_IDX = len(DEFAULT_CHARACTERS) - 1
MAX_CONSTS = len(DEFAULT_CHARACTERS) ** 2


def create_unique_const_generator(characters: str) -> Generator[str, None, None]:
    left_idx: int = 0
    right_idx: int = 0

    while right_idx != MAX_IDX + 1:
        pair: str = characters[left_idx] + characters[right_idx]

        if left_idx == MAX_IDX:
            left_idx = 0
            right_idx += 1
        else:
            left_idx += 1

        yield pair

    msg = f"cannot create more than {MAX_CONSTS} constants"
    raise OverflowError(msg)


unique_const_generator = create_unique_const_generator(DEFAULT_CHARACTERS)
