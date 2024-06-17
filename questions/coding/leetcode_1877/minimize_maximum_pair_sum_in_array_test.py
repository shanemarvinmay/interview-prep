from minimize_maximum_pair_sum_in_array_solution import *

import pytest

@pytest.mark.parametrize('message, nums, expected', [
	('Biggest + smallest is answer', [3,5,2,3], 7),
	('Answer is not biggest plus smallest', [4,1,5,1,2,5,1,5,5,4], 8)
])
def test_min_pair_sum(message, nums, expected):
	solution = Solution()

	got = solution.minPairSum(nums)

	assert got == expected, message

def test_merge_sort():
	l = [5,8,3,5]

	merge_sort(l)

	assert l == [3,5,5,8]