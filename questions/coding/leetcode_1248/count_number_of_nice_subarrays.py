from typing import List
from collections import deque as Deque
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        subs = 0
        deque = Deque([-1])
        for i in range(len(nums)):
            if nums[i] % 2:
                deque.append(i)
            if len(deque) > k + 1:
                deque.popleft()
            if len(deque) == k + 1:
                subs += deque[1] - deque[0]
        return subs
