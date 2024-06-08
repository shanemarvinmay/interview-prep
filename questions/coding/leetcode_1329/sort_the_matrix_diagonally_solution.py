from typing import List
from collections import namedtuple

class Coord:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Sort diagonals that start from first column
        for row in range(len(mat)):
            start_coord = Coord(row=row, col=0)
            end_row = len(mat) - 1
            end_col = row - len(mat) - 1
            end_coord = Coord(row=end_row, col=end_col)
            self.sort_diagonal(mat, start_coord, end_coord)
        # Sort diagonals that start from top row
        for col in range(len(mat[0])):
            start_coord = Coord(row=0, col=col)
            self.sort_diagonal(mat, start_coord)
        
    def sort_diagonal(self, mat, start_coord: Coord, end_coord=None):
        if end_coord is None:
            end_coord = self.get_end_of_diagonal(mat, start_coord)
        if start_coord.row < end_coord.row and start_coord.col < end_coord.col:
            partition_coord = self.get_partition(start_coord, end_coord, mat)
            self.sort_diagonal(mat, start_coord, Coord(partition_coord.row-1, partition_coord.col-1))
            self.sort_diagonal(mat, Coord(partition_coord.row+1, partition_coord.col+1), end_coord)
    
    def get_end_of_diagonal(self, mat, start_coord):
        end_coord = Coord(start_coord.row, start_coord.col)
        while end_coord.row < len(mat) - 1 and end_coord.col < len(mat[end_coord.row]) - 1:
            end_coord.row += 1
            end_coord.col += 1
        return end_coord

    def get_partition(self, start, end, mat):
        partition_value = mat[end.row][end.col]
        greater = Coord(row=start.row, col=start.col)
        less_equal = Coord(row=start.row, col=start.col)
        while less_equal.row < end.row and less_equal.col < end.row:
            if mat[less_equal.row][less_equal.col] <= partition_value:
                # Swapping greater and less_equal
                temp = mat[less_equal.row][less_equal.col]
                mat[less_equal.row][less_equal.col] = mat[greater.row][greater.col]
                mat[greater.row][greater.col] = temp
                greater.row += 1
                greater.col += 1
            less_equal.row += 1
            less_equal.col += 1
        # Swap pivot and greater than values
        temp = mat[end.row][end.col]
        mat[end.row][end.col] = mat[greater.row][greater.col]
        mat[greater.row][greater.col] = temp
        return greater