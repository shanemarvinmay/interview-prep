from questions.coding.leetcode_1887.reduction_operations_to_make_the_array_elements_equal import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([5,1,3], 3),
    ([1,1,1], 0),
    ([1,1,2,2,3], 4),
])
def test_reductionOperations(nums, expected):
    sol = Solution()

    got = sol.reductionOperations(nums)

    assert got == expected
