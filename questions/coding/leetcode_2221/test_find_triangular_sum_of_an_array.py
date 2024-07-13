from questions.coding.leetcode_2221.find_triangular_sum_of_an_array import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()
'''
Example 1:
Input: nums = 
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:
Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.
 

Constraints:
1 <= nums.length <= 1000
0 <= nums[i] <= 9'''
@pytest.mark.parametrize('nums, expected', [
    ([1,2,3,4,5], 8),
    ([5], 5),
])
def test_triangularSum(nums, expected, sol):
    got = sol.triangularSum(nums)

    assert got == expected
