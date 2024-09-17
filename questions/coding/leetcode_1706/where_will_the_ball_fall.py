from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        self.width = len(grid[0])
        ans = [-1] * self.width
        for col in range(self.width):
            ans[col] = self.drop_ball(col)
        return ans
    def drop_ball(self, col, row=0):
        """Given col the ball is dropped in, return destination col at the bottom of the grid.
        If the ball doesn't make it, -1 will be returned."""
        # Reached the bottom.
        if row == len(self.grid): return col
        slope_dir = self.grid[row][col]
        if slope_dir == 1:
            # Stuck on side.
            if col + 1 >= self.width:
                return -1
            # Hit a V.
            elif self.grid[row][col+1] == -1:
                return -1
            col += 1
        else: # -1
            # Stuck on side.
            if col - 1 < 0:
                return -1
            # Hit a V.
            elif self.grid[row][col-1] == 1:
                return -1
            col -= 1
        # Falling into the next row.
        return self.drop_ball(col, row+1)
