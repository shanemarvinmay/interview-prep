from questions.coding.leetcode_1004.max_consecutive_ones_iii import Solution

import pytest

'''
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
@pytest.mark.parametrize('nums, k, expected, msg', [
    ([1,1,1,0,0,0,1,1,1,1,0], 0, 4, 'K equals 0.'),
    ([0,0,1,1,1,0,0,0,1,1,1,1,0], 3, 10, '0s before, between, and after 1s'),
    ([1,1,1,0,0,0,1,1,1,1,0], 2, 6, 'Leetcode example testcase.'),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10, 'Leetcode example testcase.'),
])
def test_longestOnes(nums, k, expected, msg):
    sol = Solution()

    got = sol.longestOnes(nums, k)

    assert got == expected, msg
