from typing import List

class Solution:
    def combine(self, n: int, r: int) -> List[List[int]]:
        combos = []
        def get_combos(cur, i):
            nonlocal n, r, combos
            if len(cur) == r:
                combos.append(cur)
                return
            while i <= n:
                cur.append(i)
                get_combos(cur[:], i+1)
                cur.pop()
                i += 1
        get_combos(cur=[], i=1)
        return combos
