from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        answers = []
        
        pre = [0]
        for i in range(1, len(nums)):
            pre.append(pre[-1])
            if nums[i-1]%2 == nums[i]%2:
                pre[-1] += 1
        
        for strt, end in queries:
            if pre[end] - pre[strt] > 0:
                answers.append(False)
            else:
                answers.append(True)
        
        return answers
