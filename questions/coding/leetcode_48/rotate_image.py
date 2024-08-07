from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_rows, num_cols = len(matrix), len(matrix[0])
        # Swap row and col.
        for row in range(num_rows):
            for col in range(row, num_cols):
                self.swap_values(row, col, col, row, matrix)
        # Swap i and row len - 1 - i.
        for row in range(num_rows):
            for col in range(num_cols // 2):
                self.swap_values(row , col, row, num_cols-1-col, matrix)
        return matrix

    def swap_values(self, x1, y1, x2, y2, matrix):
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
