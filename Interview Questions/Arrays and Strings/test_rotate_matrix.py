from cgi import test
import unittest


def rotate_matrix(matrix):
    n = len(matrix)
    L = 0
    R = n - 1

    while R >= L:
        for i in range(R - L):

            # top left corner temp
            temp = matrix[L][L + i]

            # moving bottom left to top left
            matrix[L][L + i] = matrix[R - i][L]

            # moving bottom left to top left
            matrix[R - i][L] = matrix[R][R - i]

            # moving right column to bottom
            matrix[R][R - i] = matrix[L + i][R]

            # moving temp to right column
            matrix[L + i][R] = temp

        R -= 1
        L += 1
    return matrix


class test_rotate_matrix(unittest.TestCase):

    test_case_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    test_case_2 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    test_case_answer = [
        [21, 16, 11, 6, 1],
        [22, 17, 12, 7, 2],
        [23, 18, 13, 8, 3],
        [24, 19, 14, 9, 4],
        [25, 20, 15, 10, 5],
    ]

    def test_rotate_matrix(self):
        self.assertEqual(rotate_matrix(self.test_case_1[0]), self.test_case_1[1])
        self.assertEqual(rotate_matrix(self.test_case_2), self.test_case_answer)


if __name__ == "__main__":
    unittest.main()
