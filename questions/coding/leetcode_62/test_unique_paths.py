from questions.coding.leetcode_62.unique_paths import Solution

import pytest

@pytest.mark.parametrize('rows, cols, expected', [
    (3,7,28),
    (3,2,3),
])
def test_uniquePaths(rows, cols, expected):
    sol = Solution()

    got = sol.uniquePaths(rows, cols)

    assert got == expected
