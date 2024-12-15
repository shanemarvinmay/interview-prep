from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for pas, tot in classes:
            per = round(pas/tot * 100, 5)
            heapq.heappush(heap, (tot, per, pas))
        
        while extraStudents:
            tot, per, pas = heapq.heappop(heap)
            if per == 1:
                tot = 100_000
                pas = 100_000
            else:
                tot += 1
                pas += 1
                extraStudents -= 1
                per = round(pas/tot * 100, 5)
            heapq.heappush(heap, (tot, per, pas))
            
        tot = 0
        for _, percent, _ in heap:
            tot += percent
        
        avg = tot / len(heap)
        return avg / 100