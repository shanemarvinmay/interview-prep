from questions.coding.leetcode_1140.stone_game_ii import Solution

import pytest


@pytest.mark.parametrize('piles, expected', [
    ([1,2,3,4], 5),
    ([2,7,9,4,4], 10),
    ([1,2,3,4,5,100], 104),
])
def test_stoneGameII(piles, expected):
    sol = Solution()

    got = sol.stoneGameII(piles)

    assert got == expected
