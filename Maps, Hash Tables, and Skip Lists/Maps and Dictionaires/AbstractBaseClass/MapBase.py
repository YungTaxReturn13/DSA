"""Extending the MutableMapping abstract base class to provide a nonpublic _item class for use in our various map implementations"""
from typing import MutableMapping


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpubli _Item class"""

    class _Item:
        """Lightweight composite to store key-value pairs as map items"""

        __slots__ = "_key", "_value"

        def __init__(self, k, v) -> None:
            self._key = k
            self._value = v

        def __eq__(self, other: object) -> bool:  # Compare items based on their keys
            return self._key == other._key

        def __ne__(self, other: object) -> bool:  # opposite of __eq__
            return not (self == other)

        def __lt__(self, other):  # compare items based on their keys
            return self._key < other._key
