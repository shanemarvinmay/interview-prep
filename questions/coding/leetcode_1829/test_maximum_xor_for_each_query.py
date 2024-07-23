'''
Example 1:
Explanation: The queries are answered as follows:
1st query: nums = [0,1,1,3], k = 0 since 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3.
2nd query: nums = [0,1,1], k = 3 since 0 XOR 1 XOR 1 XOR 3 = 3.
3rd query: nums = [0,1], k = 2 since 0 XOR 1 XOR 2 = 3.
4th query: nums = [0], k = 3 since 0 XOR 3 = 3.
Example 2:
Input: nums = [2,3,4,7], maximumBit = 3
Output: [5,2,6,5]
Explanation: The queries are answered as follows:
1st query: nums = [2,3,4,7], k = 5 since 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7.
2nd query: nums = [2,3,4], k = 2 since 2 XOR 3 XOR 4 XOR 2 = 7.
3rd query: nums = [2,3], k = 6 since 2 XOR 3 XOR 6 = 7.
4th query: nums = [2], k = 5 since 2 XOR 5 = 7.
Example 3:
Input: nums = [0,1,2,2,5,7], maximumBit = 3
Output: [4,3,6,4,6,7]
 
Constraints:
nums.length == n
1 <= n <= 105
1 <= maximumBit <= 20
0 <= nums[i] < 2maximumBit
nums​​​ is sorted in ascending order.
'''
from questions.coding.leetcode_1829.maximum_xor_for_each_query import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, max_bit, expected', [
    ([0,1,1,3], 2, [0,3,2,3]),
])
def test_getMaximumXor(nums, max_bit, expected, sol):
    got = sol.getMaximumXor(nums, max_bit)

    assert got == expected