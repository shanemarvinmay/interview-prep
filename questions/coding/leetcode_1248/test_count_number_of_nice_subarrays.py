from questions.coding.leetcode_1248.count_number_of_nice_subarrays import Solution

import pytest

@pytest.mark.parametrize('nums, k, expected', [
    ([1,1,2,1,1], 3, 2),
    ([2,4,6], 1, 0),
    ([2,2,2,1,2,2,1,2,2,2], 2, 16),
])
def test_numberOfSubarrays(nums, k, expected):
    sol = Solution()

    got = sol.numberOfSubarrays(nums, k)

    assert got == expected
