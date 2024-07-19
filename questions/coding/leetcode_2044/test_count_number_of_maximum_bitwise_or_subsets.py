from questions.coding.leetcode_2044.count_number_of_maximum_bitwise_or_subsets import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, expected', [
    ([3,1], 2),
    ([2,2,2], 7),
    ([3,2,1,5], 6),
    # ([29,13,3,15,47,71,1,95,21,43], 528),
])
def test_countMaxOrSubsets(nums, expected, sol):
    got = sol.countMaxOrSubsets(nums)

    assert  got == expected
