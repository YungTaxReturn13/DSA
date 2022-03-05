from cgi import test
from curses.ascii import isalpha
import unittest


def pal_perm(string):
    holder = {}
    tracker = 0
    for i in string:
        if isalpha(i):
            if i.lower() in holder:
                holder[i.lower()] += 1
            else:
                holder[i.lower()] = 1

            tracker += 1

    # now need to go through the holder
    odd_trigger = tracker % 2
    for j in holder.values():
        if odd_trigger and (j % 2 == 1):
            odd_trigger -= 1
        elif j % 2 == 1:
            return False
    return True


class Test_pal_perm(unittest.TestCase):
    def test_pal_perm_true(self):
        self.assertEqual(pal_perm("aba"), True),
        self.assertEqual(pal_perm("aab"), True),
        self.assertEqual(pal_perm("abba"), True),
        self.assertEqual(pal_perm("aabb"), True),
        self.assertEqual(pal_perm("a-bba"), True),
        self.assertEqual(pal_perm("a-bba!"), True),
        self.assertEqual(pal_perm("Tact Coa"), True),
        self.assertEqual(pal_perm("jhsabckuj ahjsbckj"), True),
        self.assertEqual(pal_perm("Able was I ere I saw Elba"), True),
        self.assertEqual(pal_perm("no x in nixon"), True),
        self.assertEqual(pal_perm("azAZ"), True),

    def test_pal_perm_false(self):
        self.assertEqual(pal_perm("So patient a nurse to nurse a patient so"), False),
        self.assertEqual(pal_perm("Random Words"), False),
        self.assertEqual(pal_perm("Not a Palindrome"), False),


if __name__ == "__main__":
    unittest.main()
