from queue import Empty


class LinkedStack:
    """LIFO Stack implementation using a singly linked list for storage"""

    # --------------------------Nested _Node class----------------------------
    class _Node:
        """Lightweight, nonpublic claass for storing a singly linked node."""

        __slots__ = (
            "_element",
            "_next",
        )  # streamline memory usage as we expect to have many instances of a node class

        def __init__(self, element, next):  # Initialize node fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    # --------------------------Stack Methods---------------------------------
    def __init__(self) -> None:
        """Create an empty stack"""
        self._head = None  # reference to the head node
        self._size = 0  # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        "Return tTrue if the stack is empty"
        return self._size == 0

    def push(self, e):
        """Add element e to the top of the stack """
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack

        Raise Empty exceprtion if the stack is empty"""
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element

    def pop(self):
        """remove and return hte element from the top of the stack 
        Raise Empty excepttion if the stack is empty"""

        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    class Empty(Exception):
        pass

