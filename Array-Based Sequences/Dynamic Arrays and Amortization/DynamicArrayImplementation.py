# This simplified python list will use ctypes which allows us to get low level arrays

import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python List 
    """

    def __init__(self) -> None:
        """Create an empty array"""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n

    def __getitem__(self, k):
        """Return element at item k"""
        if not 0 <= k <= self.n:
            raise IndexError("Invalid Index")

        return self._A[k]  # Retrieve from array

    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:  # when there is not enough room
            self._resize(2 * self._capacity)  # so we double the capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):  # nonpublic utility
        """Resize internal array to capacity c"""
        B = self._make_array(c)  # new bigger array
        for k in range(self._n):  # adding in all of the existing values
            B[k] = self._A[k]
        self._A = B  # then use the bigger array
        self._capacity = c

    def _make_array(self, c):  # non public utility
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward. 
        For simplicity, we assume 0 <= k <= n in this version"""

        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Removes the first occurance of value (or raise ValueError)
        Note: we do not consider shrinking the dynamic array in this version"""

        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
            raise ValueError("value not found")

