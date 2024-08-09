from questions.coding.leetcode_885.spiral_matrix_iii import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('rows, cols, rStart, cStart, expected', [
    (1, 4, 0, 0, [[0,0],[0,1],[0,2],[0,3]]),
    (5, 6, 1, 4, [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]),
])
def test_spiralMatrixIII(rows, cols, rStart, cStart, expected, sol):
    got = sol.spiralMatrixIII(rows, cols, rStart, cStart)

    assert got == expected
