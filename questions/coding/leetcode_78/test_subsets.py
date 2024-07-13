from questions.coding.leetcode_78.subsets import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([0], [[], [0]]),
])
def test_subsets(nums, expected, sol):
    got = sol.subsets(nums)

    assert got == expected
