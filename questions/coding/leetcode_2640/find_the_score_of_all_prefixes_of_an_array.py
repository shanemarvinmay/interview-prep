from typing import List

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        cur_max = 0
        score = 0
        for i in range(len(nums)):
            cur_max = max(cur_max, nums[i])
            score += cur_max + nums[i]
            nums[i] = score
        return nums 
