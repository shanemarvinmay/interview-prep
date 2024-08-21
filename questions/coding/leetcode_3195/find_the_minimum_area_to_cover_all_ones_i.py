from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # Find top left and bottom right 1
        top, left, bottom, right = None,None,None,None

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    top = min(top, row) if top is not None else row
                    left = min(left, col) if left is not None else col
                    bottom = max(bottom, row) if bottom is not None else row
                    right = max(right, col) if right is not None else col
        
        width = max(1, right - left + 1)
        height = max(1, bottom - top + 1)

        return width * height
