from questions.coding.leetcode_498.diagonal_traverse import Solution

import pytest

@pytest.mark.parametrize('m, expected', [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,4,7,5,3,6,8,9]),
    ([[1,2],[3,4]], [1,2,3,4]),
])
def test_findDiagonalOrder(m, expected):
    sol = Solution()

    got = sol.findDiagonalOrder(m)

    assert got == expected
