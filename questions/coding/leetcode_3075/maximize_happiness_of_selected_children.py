from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        happiness.sort()
        turns = 0
        while turns < k:
            total += max(happiness.pop() - turns, 0)
            turns += 1
        return total
