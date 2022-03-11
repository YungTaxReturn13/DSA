class _DoublyLinkedBase:
    """A private bbase class providing a doubly linked list representation"""

    class _Node:
        """A lightweight, nonpublic class for storing a doubly linked node """

        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self) -> None:
        """Create an empty list"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """return the number of elements in the list"""
        return self._size

    def is_empty(self):
        """Return True if the list is empty"""
        return self._size == 0

    def _insert_betweeen(self, e, predecessor, successor):
        """Add an element e between two existing nodes and return new node"""
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delette nonsentinal node from the list and return its element """
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element  # return deleted element

