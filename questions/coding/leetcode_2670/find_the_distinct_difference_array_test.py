from find_the_distinct_difference_array_solution import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4,5], [-3,-1,1,3,5]),
    ([3,2,3,4,2], [-2,-1,0,2,3])
])
def test_distinct_difference_array(nums, expected):
    solution = Solution()

    got = solution.distinctDifferenceArray(nums)
    
    assert got == expected
