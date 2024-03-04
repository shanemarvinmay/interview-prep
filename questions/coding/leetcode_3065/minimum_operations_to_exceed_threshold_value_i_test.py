from minimum_operations_to_exceed_threshold_value_i_solution import Solution

import pytest


@pytest.mark.parametrize('message, nums, k, expected', [
    ('Some numbers smaller than k', [2, 12, 10, 1, 3], 10, 3),
    ('No numbers smaller than k', [1,1,2,4,9], 1, 0),
    ('All numbers smaller than k', [1,1,2,4,9], 10, 5),
])
def test_min_operations(message, nums, k, expected):
    solution = Solution()

    assert solution.minOperations(nums, k) == expected, message