import unittest

def one_away(s1, s2):
    # checking if the strings are the same
    if s1 == s2:
        return True

    # determining the lengths of the strings so we can decide which function to call
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len == s2_len:
        return equal_length(s1, s2)

    if abs(s1_len - s2_len) > 1:
        return False

    if s1_len > s2_len:
        return diff_length(s1, s2)

    if s2_len > s1_len:
        return diff_length(s2, s1)


def equal_length(s1, s2):
    ALLOWANCE = 1
    for i, j in enumerate(s1):
        if j != s2[i]:
            if ALLOWANCE == 0:
                return False
            else:
                ALLOWANCE -= 1
    return True


def diff_length(longer, shorter):
    counter = 0
    for i in shorter:
        if i != longer[counter]:
            counter += 1
            if i != longer[counter]:
                return False
        else:
            counter += 1

    return True


class Test(unittest.TestCase):
    def test_one_away_no_changes(self):
        # no changes
        self.assertEqual(one_away("pale", "pale"), True),
        self.assertEqual(one_away("", ""), True),

    def test_one_away_one_insert(self):
        # one insert
        self.assertEqual(one_away("ple", "pale"), True),
        self.assertEqual(one_away("pale", "ple"), True),
        self.assertEqual(one_away("pales", "pale"), True),
        self.assertEqual(one_away("ples", "pales"), True),
        self.assertEqual(one_away("pale", "pkle"), True),
        self.assertEqual(one_away("paleabc", "pleabc"), True),
        self.assertEqual(one_away("", "d"), True),
        self.assertEqual(one_away("d", "de"), True),

    def test_one_away_replace(self):
        # one replace
        self.assertEqual(one_away("pale", "bale"), True),
        self.assertEqual(one_away("a", "b"), True),
        self.assertEqual(one_away("pale", "ble"), False),

    def test_one_away_multiple_replace(self):
        # multiple replace
        self.assertEqual(one_away("pale", "bake"), False),

    def test_one_away_insert_and_replace(self):
        # insert and replace
        self.assertEqual(one_away("pale", "pse"), False),
        self.assertEqual(one_away("pale", "pas"), False),
        self.assertEqual(one_away("pas", "pale"), False),
        self.assertEqual(one_away("pkle", "pable"), False),
        self.assertEqual(one_away("pal", "palks"), False),
        self.assertEqual(one_away("palks", "pal"), False),

    def test_one_away_permutation(self):
        # permutation with insert shouldn't match
        self.assertEqual(one_away("ale", "elas"), False),


if __name__ == "__main__":
    unittest.main()
