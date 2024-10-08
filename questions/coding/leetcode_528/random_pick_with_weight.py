from typing import List
from random import random

class Solution:
    def __init__(self, w: List[int]):
        self.total = w[0]
        for i in range(1, len(w)):
            self.total += w[i]
            w[i] += w[i-1]
        self.w = w
        print(f'w:{w}')
    def pickIndex(self) -> int:
        target = self.total * random()
        l = 0
        r = len(self.w)
        while l < r:
            m = (l+r) // 2
            if self.w[m] < target:
                l = m + 1
            elif self.w[m] > target:
                r = m 
            else:
                return m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()