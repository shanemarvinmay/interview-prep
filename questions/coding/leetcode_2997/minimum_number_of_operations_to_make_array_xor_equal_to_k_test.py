from minimum_number_of_operations_to_make_array_xor_equal_to_k_solution import Solution

import pytest 

@pytest.mark.parametrize("nums, k, expected, message", [
	([2, 1, 3, 4], 1, 2, "Compute xor correctly"),
	([4], 9, 3, "XOR result has more bits than k"),
	([9], 4, 3, "XOR result has less bits than k")
])
def test_min_operations(nums, k, expected, message):
	solution = Solution()

	got = solution.minOperations(nums, k)

	assert got == expected, message
