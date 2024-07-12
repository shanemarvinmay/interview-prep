from questions.coding.leetcode_2442.count_number_of_distinct_integers_after_reverse_operations import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, expected', [
    ([1,13,10,12,31], 6),
    ([2,2,2], 1),
])
def test_countDistinctIntegers(nums, expected, sol):
    got = sol.countDistinctIntegers(nums)

    assert got == expected
