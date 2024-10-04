from typing import List
from collections import deque

'''
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        bg = 0
        flipped = deque()
        n = len(nums)
        start, end = 0, 0
        while end < n:
            if nums[end] == 0:
                flipped.append(end)
                if len(flipped) > k:
                    start = flipped.popleft() + 1
            end += 1
            bg = max(bg, end-start)
        return bg
