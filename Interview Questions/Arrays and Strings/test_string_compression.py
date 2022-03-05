import string
import unittest


def string_compression(string):
    compressed = []
    holder = ""
    count = 0

    for i in string:
        if i != holder:
            if holder != "":
                compressed.append(holder)
            if count != 0:
                compressed.append(str(count))
            holder = i
            count = 1
        else:
            count += 1
    compressed.append(holder)
    compressed.append(str(count))
    if len(string) > len(compressed):
        return "".join(compressed)
    else:
        return string


class test(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compression("abcdef"), "abcdef")
        self.assertEqual(string_compression("aabb"), "aabb")
        self.assertEqual(string_compression("aaa"), "a3")
        self.assertEqual(string_compression("a"), "a")
        self.assertEqual(string_compression(""), "")


if __name__ == "__main__":
    unittest.main()
