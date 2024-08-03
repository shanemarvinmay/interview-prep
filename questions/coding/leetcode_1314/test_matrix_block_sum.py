from questions.coding.leetcode_1314.matrix_block_sum import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def matrix():
    return [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]

@pytest.mark.parametrize('k, expected', [
    (1, [
        [12,21,16],
        [27,45,33],
        [24,39,28]
    ]),
    (2, [[45,45,45],[45,45,45],[45,45,45]]),
])
def test_matrixBlockSum(k, expected, sol, matrix):
    got = sol.matrixBlockSum(matrix, k)

    assert got == expected

@pytest.mark.parametrize('message, start_row, end_row, start_col, end_col, expected', [
    ('Need to subtract col to left.', 0, 1, 1, 2, 16),
    ('No col to subtract.', 1, 1, 0, 1, 9),
])
def test_get_rect_sum(message, start_row, end_row, start_col, end_col, expected, sol, matrix):
    sol.set_row_sum_matrix(matrix)

    got = sol.get_rect_sum(start_row, end_row, start_col, end_col)

    assert got == expected, message

@pytest.mark.parametrize('message, row, col, k, expected', [
    ('Out of range.', 0, 0, 4, (0,2,0,2)),
    ('In range.', 1, 1, 0, (1,1,1,1)),
])
def test_get_cols_rows(message, row, col, k, expected, sol, matrix):
    got = sol.get_cols_rows(row, col, matrix, k)

    assert got == expected, message

def test_set_row_sum_matrix(sol, matrix):
    expected = [
        [1,3,6],
        [4,9,15],
        [7,15,24]
    ]

    sol.set_row_sum_matrix(matrix)
    got = sol.sum_matrix

    assert got == expected