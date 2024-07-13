from questions.coding.leetcode_46.permutations import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1], [[0,1],[1,0]]),
    ([1], [[1]]),
])
def test_permute(nums, expected, sol):
    got = sol.permute(nums)

    assert got == expected
