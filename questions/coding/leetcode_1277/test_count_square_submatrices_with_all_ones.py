from questions.coding.leetcode_1277.count_square_submatrices_with_all_ones import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('matrix, expected', [
    ([
    [0,1,1,1],
    [1,1,1,1],
    [0,1,1,1]
    ], 15),
    ([
    [1,0,1],
    [1,1,0],
    [1,1,0]
    ], 7),
])
def test_countSquares(matrix, expected, sol):
    got = sol.countSquares(matrix)

    assert got == expected
