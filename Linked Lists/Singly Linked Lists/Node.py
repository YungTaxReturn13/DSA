class _Node:
    """Lightweight, nonpublic claass for storing a singly linked node."""

    __slots__ = (
        "_element",
        "_next",
    )  # streamline memory usage as we expect to have many instances of a node class

    def __init__(self, element, next):  # Initialize node fields
        self._element = element  # reference to user's element
        self._next = next  # reference to next node
