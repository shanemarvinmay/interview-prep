from typing import List

class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n # starting at 1 to include the num we are on

        # Adding whats <= val on the left
        s = [] # monotomic stack (val, idx)
        for i, val in enumerate(nums):
            # rm small values from stack
            while s and s[-1][0] < val:
                s.pop()
            # Adding how many <= values on the left
            if s:
                res[i] += i - s[-1][1] - 1
            else:
                res[i] += i
            # Appending current val and index to stack
            s.append((val, i))

        # Adding whats <= val on the right
        # Emptying the stack
        s = [] # monotomic stack (val, idx)
        for i in range(n-1, -1, -1):
            val = nums[i]
            # rm small values from stack
            while s and s[-1][0] < val:
                s.pop()
            # Adding how many <= values on the right
            if s:
                res[i] += s[-1][1] - i - 1 # -1 to exclude the num we are on
            else:
                res[i] += n - i - 1 # -1 to exclude the num we are on
            # Appending current val and index to stack
            s.append((val, i))
        
        return res
