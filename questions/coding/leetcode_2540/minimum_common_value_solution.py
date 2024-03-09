class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        idx1, idx2 = 0, 0
        # Could have done a binary search to find if one num was in the other list.
        # Or put one list into a map. Then go through the other and find the minimum present.
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] == nums2[idx2]:
                return nums1[idx1]
            elif nums1[idx1] < nums2[idx2]:
                idx1 += 1
            else:
                idx2 += 1
        
        return -1
