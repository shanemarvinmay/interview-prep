from find_the_xor_of_numbers_which_appear_twice_solution import Solution

import pytest

@pytest.mark.parametrize("nums, expected, message", [
	([1,2,3], 0, "No duplicates."),
	([1,2,1,3], 1, "One duplicate."),
	([1,2,2,1], 3, "Mutliple duplicates."),
])
def test_duplicate_number_xor(nums, expected, message):
	solution = Solution()

	got = solution.duplicateNumbersXOR(nums) 

	assert got == expected, message
