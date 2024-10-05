from questions.coding.leetcode_1874.minimize_product_sum_of_two_arrays import Solution

import pytest

'''
Constraints:
n == nums1.length == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 100
'''

@pytest.mark.parametrize('nums1, nums2, expected', [
    ([5,3,4,2], [4,2,2,5], 40),
    ([2,1,4,5,7], [3,2,4,8,6], 65),
])
def test_minProductSum(nums1, nums2, expected):
    sol = Solution()

    got = sol.minProductSum(nums1, nums2)

    assert got == expected
