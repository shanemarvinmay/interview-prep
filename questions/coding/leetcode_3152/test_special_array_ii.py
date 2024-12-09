from questions.coding.leetcode_3152.special_array_ii import Solution

import pytest

@pytest.mark.parametrize('nums, queries, expected', [
    ([3,4,1,2,6], [[0,4]], [False]),
    ([4,3,1,6], [[0,2],[2,3]], [False, True])
])
def test_isArraySpecial(nums, queries, expected):
    sol = Solution()

    got = sol.isArraySpecial(nums, queries)

    assert got == expected
