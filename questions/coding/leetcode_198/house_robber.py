from typing import List

class Solution:
    def rob(self, houses: List[int]) -> int:
        a = b = 0

        for i in range(len(houses)):
            if i % 2:
                a = max(a+houses[i], b)
            else:
                b = max(b+houses[i], a)
        
        return max(a, b)
