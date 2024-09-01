from questions.coding.leetcode_2275.largest_combination_with_bitwise_and_greater_than_zero import Solution

import pytest

@pytest.mark.parametrize('candidates, expected', [
    ([16,17,71,62,12,24,14], 4),
    ([8,8], 2),
])
def test_largestCombination(candidates, expected):
    sol = Solution()

    got = sol.largestCombination(candidates)

    assert got == expected
