from questions.coding.leetcode_1940.longest_common_subsequence_between_sorted_arrays import Solution

import pytest

@pytest.mark.parametrize('ars, expected',[
    ([[1,3,4],
    [1,4,7,9]],
    [1,4]),
    ([[2,3,6,8],
    [1,2,3,5,6,7,10],
    [2,3,4,6,9]],
    [2,3,6]),
    ([[1,2,3,4,5],
    [6,7,8]],
    []),
])
def test_longestCommonSubsequence(ars, expected):
    sol = Solution()

    got = sol.longestCommonSubsequence(ars)

    assert got == expected
