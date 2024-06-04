from typing import List
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1 = sum(nums1)
        sum_2 = sum(nums2)
        diff = sum_2 - sum_1
        return diff // len(nums1)
