from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        num_dups = 0
        i = len(nums) - 1

        while i >= 0:
            if num_dups > i:
                break
            if nums[i] in seen:
                nums[num_dups], nums[i] = nums[i], nums[num_dups]
                num_dups += 1
                continue
            seen.add(nums[i])
            i -= 1
            
        
        return nums[:num_dups]
