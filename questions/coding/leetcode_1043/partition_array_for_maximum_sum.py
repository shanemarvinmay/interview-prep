from typing import List

class Solution:
    def maxSumAfterPartitioning(self, ar: List[int], k: int) -> int:
        cache = dict()

        def dfs(i):
            if i in cache:
                return cache[i]
            cur_max = 0
            res = 0
            for j in range(i, min(len(ar), i+k)):
                cur_max = max(cur_max, ar[j])
                window_size = j - i + 1
                res = max(res, dfs(j+1) + cur_max * window_size)
            cache[i] = res
            return res
        
        return dfs(0)
