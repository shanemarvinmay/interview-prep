from questions.coding.leetcode_1727.largest_submatrix_with_rearrangements import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('matrix, expected', [
    ([[0,0,1],[1,1,1],[1,0,1]], 4),
    ([[1,0,1,0,1]], 3),
    ([[1,1,0],[1,0,1]], 2),
])
def test_largestSubmatrix(matrix, expected, sol):
    got = sol.largestSubmatrix(matrix)

    assert got == expected
