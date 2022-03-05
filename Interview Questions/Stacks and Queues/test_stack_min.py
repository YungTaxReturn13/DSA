import unittest


class StackMin:
    def __init__(self):
        self._data = []
        self._min_tracker = []

    def pop(self):
        if len(self._data) == 0:
            raise Exception("The stack is empty")
        x = self._data.pop()
        if x == self._min_tracker[-1]:
            self._min_tracker.pop()
        return x

    def push(self, e):
        if len(self._min_tracker) == 0 or e <= self._min_tracker[-1]:
            self._min_tracker.append(e)
        self._data.append(e)

    def minimum(self):
        if len(self._min_tracker) == 0:
            return None
        return self._min_tracker[-1]


class test_stack_min(unittest.TestCase):
    def test_min_stack(self):

        newstack = StackMin()
        assert newstack.minimum() is None

        newstack.push(5)
        assert newstack.minimum() == 5

        newstack.push(6)
        assert newstack.minimum() == 5

        newstack.push(3)
        assert newstack.minimum() == 3

        newstack.push(7)
        assert newstack.minimum() == 3

        newstack.push(3)
        assert newstack.minimum() == 3

        newstack.pop()
        assert newstack.minimum() == 3

        newstack.pop()
        assert newstack.minimum() == 3

        newstack.pop()
        assert newstack.minimum() == 5

        newstack.push(1)
        assert newstack.minimum() == 1


if __name__ == "__main__":
    unittest.main()
