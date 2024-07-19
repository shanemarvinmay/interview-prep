from typing import List

class Solution:
    def __init__(self):
        self.matrix = []
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        self.row_sums = rowSum
        self.col_sums = colSum
        self.init_matrix()
        
    def init_matrix(self):
        n = len(self.row_sums)
        for row in self.row_sums:
            self.matrix.append([])
            for col in self.col_sums:
                num = (row + col) // n
                self.matrix[-1].append(num)
