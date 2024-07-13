from questions.coding.leetcode_78.subsets import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()
"""
Example 1:
Input: nums = 
Output: 
Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique."""
@pytest.mark.parametrize('nums, expected', [
    ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ([0], [[], [0]]),
])
def test_subsets(nums, expected, sol):
    got = sol.subsets(nums)

    assert got == expected
