from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        # building the matrix
        m = []
        for _ in range(len(grid)):
            row = []
            for _ in range(len(grid[0])):
                row.append(0)
            m.append(row)
        # finding diffs of distinct values
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                m[row][col] = abs(self.get_unique_left_up(grid, row, col) - self.get_unique_right_down(grid, row, col))
        return m
    def get_unique_left_up(self, grid, row, col):
        unique = set()
        row -= 1
        col -= 1
        while row >= 0 and col >= 0:
            unique.add(grid[row][col])
            row -= 1
            col -= 1
        return len(unique)
    def get_unique_right_down(self, grid, row, col):
        unique = set()
        row += 1
        col += 1
        while row < len(grid) and col < len(grid[0]):
            unique.add(grid[row][col])
            row += 1
            col += 1
        return len(unique)
