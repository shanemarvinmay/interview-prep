class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set, nums2_set = set(nums1), set(nums2)

        unique_nums1 = [num for num in nums1_set if num not in nums2_set]
        unique_nums2 = [num for num in nums2_set if num not in nums1_set]

        # unique_nums1 = list(nums1_set.difference(nums2_set))
        # unique_nums2 = list(nums2_set.difference(nums1_set))

        return [unique_nums1, unique_nums2]