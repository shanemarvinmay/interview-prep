from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()

        bg = l = r = 0
        while r < len(nums):
            while r < len(nums) and abs(nums[r] - nums[l]) <= k * 2:
                r += 1
            bg = max(bg, r - l)
            l += 1

        return bg
