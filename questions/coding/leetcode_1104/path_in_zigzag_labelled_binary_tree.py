from typing import List
from math import floor, log2
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label:
            path.append(label)
            lvl = floor(log2(label))
            lvl_max = 2 ** (lvl+1) - 1
            lvl_min = 2 ** lvl
            inverse = lvl_max + lvl_min - label
            # Parent
            label = inverse // 2
            
        path.reverse()
        return path