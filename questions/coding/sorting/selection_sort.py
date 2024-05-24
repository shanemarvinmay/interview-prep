"""This was an example problem on Leetcode to practice selection sort."""
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            # Finding the index of the smallest number.
            # But only look at the indices from i to nums length - 1.
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            # Swapping the number at index i with the smallest number.
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        
        return nums
            
            