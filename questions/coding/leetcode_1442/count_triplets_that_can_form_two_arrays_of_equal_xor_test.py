from count_triplets_that_can_form_two_arrays_of_equal_xor_solution import Solution

import pytest


@pytest.mark.parametrize("ar, expected", [
	([2,3,1,6,7], 4),
	([1,1,1,1,1], 10)
])
def test_count_triplets(ar, expected):
	solution = Solution()

	got = solution.countTriplets(ar)

	assert got == expected
