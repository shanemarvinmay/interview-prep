from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        cur_row = 0
        cur_col = 0
        
        # Init matrix
        matrix = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(0)
            matrix.append(row)

        while cur_row < rows or cur_col < cols:
            if cur_row >= rows:
                matrix[-1][cur_col] = colSum[cur_col]
                cur_col += 1
                continue
            if cur_col >= cols:
                matrix[cur_row][-1] = rowSum[cur_row]
                cur_row += 1
                continue

            value = min(rowSum[cur_row], colSum[cur_col])
            rowSum[cur_row] -= value
            colSum[cur_col] -= value
            matrix[cur_row][cur_col] = value

            if rowSum[cur_row] == 0:
                cur_row += 1
            if colSum[cur_col] == 0:
                cur_col += 1
        
        return matrix
