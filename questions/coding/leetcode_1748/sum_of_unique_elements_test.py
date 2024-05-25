from collections import namedtuple
from sum_of_unique_elements_solution import Solution

import pytest

EdgeCase = namedtuple('EdgeCase', 'nums, expected, message')
@pytest.mark.parametrize('nums, expected, message', [
    EdgeCase(nums=[1,1,1,1,1], expected=0, message="No unique numbers."),
    EdgeCase(nums=[1,2,3,2], expected=4, message="Some unique numbers."),
    EdgeCase(nums=[1,2,3,4,5], expected=15, message="All unique numbers."),
])
def test_sum_of_unique(nums, expected, message):
    solution = Solution()

    assert solution.sumOfUnique(nums) == expected, message
