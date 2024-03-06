from subarrays_distinct_element_sum_of_squares_i_solution import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([1,2,1], 15),
    ([1,1], 3)
])
def test_sum_count(nums, expected):
    solution = Solution()

    assert solution.sumCounts(nums) == expected