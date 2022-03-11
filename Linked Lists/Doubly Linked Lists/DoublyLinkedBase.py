class _DoublyLinkedBase:
    """A private bbase class providing a doubly linked list representation"""

    class _Node:
        """A lightweight, nonpublic class for storing a doubly linked node """

        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._prev = prev
            self._next = next

