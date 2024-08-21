from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        sub_count = 1
        
        nums.sort()

        cur_min = nums[0]
        for num in nums:
            if num - cur_min > k:
                sub_count += 1
                cur_min = num
        
        return sub_count
