from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        for pas, tot in classes:
            potential = ((pas+1) / (tot+1))
            cur = (pas/tot)
            impact = ((pas+1) / (tot+1)) - (pas/tot)
            heapq.heappush(heap, (impact * -1, tot, pas))
        
        while extraStudents:
            impact, tot, pas = heapq.heappop(heap)
            if impact == 0: 
                heapq.heappush(heap, (impact * -1, tot, pas))
                break
            tot += 1
            pas += 1
            extraStudents -= 1
            impact = ((pas+1) / (tot+1)) - (pas/tot)
            heapq.heappush(heap, (impact * -1, tot, pas))
            
        total = 0
        for impact, tot, pas in heap:
            total += (pas / tot)
        
        avg = total / len(heap)
        return avg