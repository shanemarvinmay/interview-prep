from typing import List

class Solution:
    def __init__(self):
        self.sum_matrix = []
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        self.set_row_sum_matrix(mat)

        num_rows, num_cols  = len(mat), len(mat[0])
        for row in range(num_rows):
            for col in range(num_cols):
                start_row, end_row, start_col, end_col = self.get_cols_rows(row, col, mat, k)
                mat[row][col] = self.get_rect_sum(start_row, end_row, start_col, end_col)
        
        return mat
    
    def get_rect_sum(self, start_row, end_row, start_col, end_col):
        total = 0
        for row in range(start_row, end_row+1):
            total += self.sum_matrix[row][end_col]
            if start_col > 0:
                total -= self.sum_matrix[row][start_col-1]
        return total

    def get_cols_rows(self, row, col, mat, k):
        start_row = max(0, row-k)
        end_row = min(len(mat)-1, row+k)
        start_col = max(0, col-k)
        end_col = min(len(mat[0])-1, col+k)
        return start_row, end_row, start_col, end_col
    
    def set_row_sum_matrix(self, mat):
        self.sum_matrix = []
        for row in range(len(mat)):
            self.sum_matrix.append([])
            row_sum = 0
            for col in range(len(mat[row])):
                row_sum += mat[row][col]
                self.sum_matrix[-1].append(row_sum)
