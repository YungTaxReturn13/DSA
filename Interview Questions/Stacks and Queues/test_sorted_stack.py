import unittest


import unittest


class SortedStack:
    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if len(self._data) == 0:
            return False
        return self._data.pop()

    def __len__(self):
        return len(self._data)

    def sort(self):
        temp_stack = []
        trigger = True

        while trigger:
            counter = 1
            temp_var = self._data.pop()
            for _ in range(len(self._data)):
                if self._data[-1] < temp_var:
                    temp_stack.append(self._data.pop())
                    counter += 1
                else:
                    temp_stack.append(temp_var)
                    temp_var = self._data.pop()

            temp_stack.append(temp_var)
            for _ in range(len(temp_stack)):
                self._data.append(temp_stack.pop())

            if counter - 1 == 0:
                trigger = False


class testSortedStack(unittest.TestCase):
    def test_push_one(self):
        queue = SortedStack()
        queue.push(1)
        queue.sort()
        assert len(queue) == 1

    def test_push_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.sort()
        assert len(queue) == 2

    def test_push_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.sort()
        assert len(queue) == 3

    def test_pop_one(self):
        queue = SortedStack()
        queue.push(1)
        queue.sort()
        assert queue.pop() == 1

    def test_pop_two(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.sort()
        assert queue.pop() == 1
        assert queue.pop() == 2

    def test_pop_three(self):
        queue = SortedStack()
        queue.push(1)
        queue.push(2)
        queue.push(3)
        queue.sort()
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3

    def test_push_mixed(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(1)
        queue.push(4)
        queue.sort()
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4


if __name__ == "__main__":
    unittest.main()
