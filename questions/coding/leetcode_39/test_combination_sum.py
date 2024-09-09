from questions.coding.leetcode_39.combination_sum import Solution

import pytest

@pytest.mark.parametrize('candidates, target, expected', [
    ([2,3,6,7], 7, [[2,2,3],[7]]),
    ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ([2], 1, []),
])
def test_combinationSum(candidates, target, expected):
    sol = Solution()

    got = sol.combinationSum(candidates, target)

    assert sorted(got) == sorted(expected)
