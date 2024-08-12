from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        bg = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[row])-2):
                hr = (grid[row][col] + grid[row][col+1] + grid[row][col+2] +
                grid[row+1][col+1] +
                grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]
                )
                bg = max(bg, hr)
        return bg