from questions.coding.leetcode_2966.divide_array_into_arrays_with_max_difference import Solution

import pytest

@pytest.mark.parametrize('nums, k, expected', [
    ([1,3,4,8,7,9,3,5,1], 2, [[1,1,3],[3,4,5],[7,8,9]]),
    ([2,4,2,2,5,2], 2, []),
    ([4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], 14, [[2,2,2],[4,5,5],[5,5,7],[7,8,8],[9,9,10],[11,12,12]]),
])
def test_divideArray(nums, k, expected):
    sol = Solution()

    got = sol.divideArray(nums, k)

    assert got == expected
