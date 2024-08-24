from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        output = []
        x_idxs = []
        for i in range(len(nums)):
            if nums[i] == x:
                x_idxs.append(i)
        
        for query in queries:
            if query > len(x_idxs):
                output.append(-1)
            else:
                output.append(x_idxs[query-1])
        
        return output
    