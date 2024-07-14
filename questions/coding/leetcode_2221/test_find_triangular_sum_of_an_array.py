from questions.coding.leetcode_2221.find_triangular_sum_of_an_array import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4,5], 8),
    ([5], 5),
])
def test_triangularSum(nums, expected, sol):
    got = sol.triangularSum(nums)

    assert got == expected
