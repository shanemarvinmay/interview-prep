from typing import List

'''
1874. Minimize Product Sum of Two Arrays
https://leetcode.com/problems/minimize-product-sum-of-two-arrays/
Constraints:
n == nums1.length == nums2.length
1 <= n <= 105
1 <= nums1[i], nums2[i] <= 100
'''

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        product = 0

        nums1.sort()
        nums2.sort(reverse=True)

        for i in range(len(nums1)):
            product += nums1[i] * nums2[i]
        
        return product
