from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        inc = [0] * N
        dec = [0] * N

        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], inc[j]+1)
        for i in range(N-1, -1, -1):
            for j in range(N-1, i, -1):
                if nums[i] > nums[j]:
                    dec[j] = max(dec[i], dec[j]+1)
        
        sm = float('inf')
        for i in range(N):
            if inc[i] and dec[i]:
                sm = min(sm, N - inc[i] - dec[i])
        
        return sm