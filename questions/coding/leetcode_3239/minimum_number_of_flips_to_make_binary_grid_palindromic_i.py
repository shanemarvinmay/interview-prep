from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        horizontal_flips = vertical_flips = 0

        # Checking horizontal changes needed.
        for row in grid:
            for col in range(len(row) // 2):
                left_big = row[col]
                right_bit = row[len(row)-1 - col]
                if left_big != right_bit:
                    horizontal_flips += 1
        
        # Checking vertical changes needed.
        for col in range(len(grid[0])):
            for row in range(len(grid) // 2):
                top_bit = grid[row][col]
                bottom_bit = grid[len(grid)-1 - row][col]
                if top_bit != bottom_bit:
                    vertical_flips += 1
        
        return min(horizontal_flips, vertical_flips)
