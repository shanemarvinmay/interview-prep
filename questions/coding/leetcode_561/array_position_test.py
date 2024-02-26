from array_position_solution import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([1,4,3,2], 4),
    ([6,2,6,5,1,2], 9)
])
def test_array_pair_sum(nums, expected):
    solution = Solution()

    assert solution.arrayPairSum(nums) == expected
