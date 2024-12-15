from questions.coding.leetcode_2762.continuous_subarrays import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([5,4,2,4], 8),
    ([1,2,3], 6),
])
def test_continuousSubarrays(nums, expected):
    sol = Solution()

    got = sol.continuousSubarrays(nums)

    assert got == expected
