from minimum_operations_to_make_the_array_increasing_solution import Solution

import pytest


@pytest.mark.parametrize('nums, expected, message', [
    ([1,1,1], 3, 'No new max.'),
    ([1,5,2,4,1], 14, 'One new max.'),
    ([8], 0, 'Only one element.'),
    ([1,2,3], 0, 'No moves needed.')
])
def test_min_operations(nums, expected, message):
    solution = Solution()

    assert solution.minOperations(nums) == expected, message