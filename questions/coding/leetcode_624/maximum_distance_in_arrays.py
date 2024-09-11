from typing import List

class Solution:
    def maxDistance(self, ars: List[List[int]]) -> int:
        # smallest/biggest at 0, next smallest/biggest at 1.
        smalls, bigs = [], []
        for ar in ars:
            sm, bg = ar[0], ar[-1]
            if len(smalls) < 2:
                smalls.append(sm)
            if len(bigs) < 2:
                bigs.append(bg)
            
'''
m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
'''