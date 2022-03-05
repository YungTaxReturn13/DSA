import unittest


class SetOfStacks:
    def __init__(self, limit):
        self._data = []
        self._limit = limit

    def push(self, e):
        if len(self._data) == 0 or len(self._data[-1]) == self._limit:
            self._data.append([])
        self._data[-1].append(e)

    def pop(self):
        if len(self._data[-1]) == 0:
            self._data.pop()
        return self._data[-1].pop()

    def pop_at(self, i):
        if len(self._data[i]) == 0:
            self._data.pop(i)
        return self._data[i].pop()


class testSetOfStacks(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        assert lst == list(reversed(range(35)))

    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        assert lst == list(range(35, 4))


if __name__ == "__main__":
    unittest.main()
