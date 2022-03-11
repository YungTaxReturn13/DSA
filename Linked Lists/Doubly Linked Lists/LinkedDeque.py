from DoublyLinkedBase import _DoublyLinkedBase


class Empty(Exception):
    pass


class LinkedDeque(_DoublyLinkedBase):  # note the use of inheritence
    """Double-ended queue implementation based on a double linked list"""

    def first(self):
        """Return but do not remove the element at the front of the deque"""

        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element  # real item just after the header

    def last(self):
        """Return but do not remove the element at the back of the deque"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element  # real item just before trailer

    def insert_first(self, e):
        """Add an element to the front of the deque"""
        self._insert_betweeen(e, self._header, self._header._next)  # after header

    def insert_last(self, e):
        """Add an element to the back of the deque"""
        self._insert_betweeen(e, self._trailer._prev, self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque
        
        Raise Empty exception if the deque is empty"""

        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)  # use inherited method

    def delete_last(self):
        """Remove and return the element form the back of the deque 

        Raise Empty exception if the deque is empty 
        """

        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
