import unittest


class MyQueue:
    def __init__(self) -> None:
        self._stack1 = []
        self._stack2 = []
        self._condition = True

    def add(self, e):
        if self._condition:
            self._stack1.append(e)
        else:
            for _ in range(len(self._stack2)):
                self._stack1.append(self._stack2.pop())
            self._condition = True

    def remove(self):
        if not self._condition:
            if self.is_empty():
                return False
            else:
                return self._stack2.pop()
        else:
            for _ in range(len(self._stack1)):
                self._stack2.append(self._stack1.pop())
            if self.is_empty():
                return False
            return self._stack2.pop()

    def is_empty(self):
        if self._condition:
            return len(self._stack2) == 0
        else:
            return len(self._stack1) == 0

    def __len__(self):
        if self._condition:
            return len(self._stack1)
        else:
            return len(self._stack2)

    def peek(self):
        if not self._condition:
            return self._stack2[-1]
        else:
            return self._stack1[0]


class testMyQueue(unittest.TestCase):
    test_cases = [([1, 2, 3]), ([-1, 0, 1]), (["a", "b", "c", "d", "e", "f"])]

    def test_size(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for index, val in enumerate(sequence, start=1):
                q.add(val)
                assert len(q) == index
            for index, val in enumerate(sequence, start=1):
                q.remove()
                assert 0 == 0
            assert len(q) == len(sequence) - index

    def test_add(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            assert q.peek() == sequence[0]
            assert len(q) == len(sequence)

    def test_remove(self):
        for sequence in self.test_cases:
            q = MyQueue()
            for val in sequence:
                q.add(val)
            for i in range(len(sequence)):  # noqa
                assert q.remove() == sequence[i]

    def test_peek_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4

    def test_add_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert q.peek() == 4
        q.add(101)
        assert q.peek() != 101

    def test_remove_simple(self):
        q = MyQueue()
        q.add(4)
        q.add(6)
        assert len(q) == 2
        assert q.remove() == 4
        assert q.remove() == 6
        assert len(q) == 0
        assert not q.remove()


if __name__ == "__main__":
    unittest.main()
