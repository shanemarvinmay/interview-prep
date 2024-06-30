from find_the_prefix_common_array_of_two_arrays import Solution

import pytest

@pytest.mark.parametrize("a, b, expected", [
	([1,3,2,4], [3,1,2,4], [0,2,3,4]),
	([2,3,1],[3,1,2],[0,1,3]),
	([1,2,3], [3,1,2], [0,1,3])
])
def test_find_the_prefix_common_array(a, b, expected):
	solution = Solution()

	got = solution.findThePrefixCommonArray(a, b)

	assert got == expected
