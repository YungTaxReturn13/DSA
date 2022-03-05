import unittest


def zero_matrix(matrix):
    n_rows = len(matrix)
    n_columns = len(matrix[0])

    row_zero = False
    column_zero = False

    # Going through and checking if there are any zeros in the first column and row
    for i in matrix[0]:
        if i == 0:
            row_zero = True
    for i in matrix:
        if i[0] == 0:
            column_zero = True

    # bulk of the zeroes get identified here
    for i in range(1, n_rows):
        for j in range(1, n_columns):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # converting columns
    for i, j in enumerate(matrix[0]):
        if j == 0:
            for x in range(n_rows):
                matrix[x][i] = 0

    # converting rows
    for i, j in enumerate(matrix):
        if j[0] == 0:
            for x in range(n_columns):
                matrix[i][x] = 0

    # converting the top row and first column if necessary
    if row_zero:
        for i in range(n_columns):
            matrix[0][i] = 0

    if column_zero:
        for i in range(n_rows):
            matrix[i][0] = 0

    return matrix


test_cases = [
    [
        [1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ],
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [11, 0, 13, 14, 0],
        [0, 0, 0, 0, 0],
        [21, 0, 23, 24, 0],
    ],
]


class test_zero_matrix(unittest.TestCase):
    def test_zero_matrix(self):
        self.assertEqual(zero_matrix(test_cases[0]), test_cases[1])


if __name__ == "__main__":
    unittest.main()
