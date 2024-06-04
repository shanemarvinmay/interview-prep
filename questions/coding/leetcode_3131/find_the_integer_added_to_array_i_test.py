from find_the_integer_added_to_array_i_solution import Solution

import pytest

@pytest.mark.parametrize("nums1, nums2, expected", [
	([2,6,4], [9,7,5], 3),
	([10], [5], -5),
	([1,1,1,1], [1,1,1,1], 0)
])
def test_add_integer(nums1, nums2, expected):
	solution = Solution()

	assert solution.addedInteger(nums1, nums2) == expected