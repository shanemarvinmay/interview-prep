from typing import List
from random import randint
from collections import defaultdict

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        bg = 1
        hm = defaultdict(int)
        for row in range(len(matrix)):
            zero, one = 0, 0
            for col in range(len(matrix[row])):
                if matrix[row][col]:
                    one += 2**col
                else:
                    zero += 2**col
            hm[(zero, one)] += 1
            hm[(one, zero)] += 1
            bg = max(bg, hm[(zero, one)])
        return bg

def gen_m(rows=3, cols=3):
    for _ in range(rows):
        for _ in range(cols):
            print(randint(0,1), end=' ')
        print()

# gen_m(4, 3)