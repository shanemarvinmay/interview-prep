from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        last_idx = len(nums) - 1
        for i in range(last_idx, 0, -1):
            for j in range(i):
                nums[j] = (nums[j] + nums[j+1]) % 10
        return nums[0]