from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for i in range(len(nums)):
            num_subsets = len(subsets)
            for j in range(num_subsets):
                subset = subsets[j][:]
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                subsets.append(subset)
        
        return subsets
