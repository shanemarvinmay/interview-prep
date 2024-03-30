from find_greatest_common_divisor_of_array_solution import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([2,5,6,9,10], 2),
    ([7,5,6,8,3], 1),
    ([3,3], 3),
])
def test_find_gcd(nums, expected):
    solution = Solution()

    assert solution.findGCD(nums) == expected