from questions.coding.leetcode_198.house_robber import Solution

import pytest

@pytest.mark.parametrize('houses, expected', [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
])
def test_rob(houses, expected):
    sol = Solution()

    got = sol.rob(houses)

    assert got == expected
