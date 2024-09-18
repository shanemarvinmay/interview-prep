from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(0, len(nums), 3):
            out_of_range = abs(nums[i] - nums[i+1]) > k
            out_of_range = out_of_range or abs(nums[i] - nums[i+2]) > k
            out_of_range = out_of_range or abs(nums[i+1] - nums[i+2]) > k
            if out_of_range:
                return []
            output.append([nums[i],nums[i+1],nums[i+2]])
        
        return output
