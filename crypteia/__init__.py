from typing import Callable

from .converters import ToBytes, ToString
from .multibasing import Multibasing
from .multihashing import Multihashing

__all__ = ["ToBytes", "ToString", "Multibasing", "Multihashing", "compose"]


def compose(to_bytes, multihasher, multibaser) -> Callable[[str], str]:
    def get_hash(data):
        bin_data = to_bytes(data)
        hashed_data = multihasher(bin_data)
        encoded_data = multibaser.encode(hashed_data)
        return encoded_data

    return get_hash
