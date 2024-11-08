from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bg = 0
        self.seen = dict() # {row: {col}}
        q = deque()
        self.rows = len(grid)
        self.cols = len(grid[0])
        oranges = 0
        empty = 0
        # finding all of the rottens
        for row in range(self.rows):
            for col in range(self.cols):
                # Is rotten
                if grid[row][col] == 2:
                    # row, col, time
                    q.append((row, col, 0))
                    self.record_seen(row, col)
                elif grid[row][col] == 1:
                    oranges += 1
                else:
                    empty += 1
        rotten = len(q)
        if len(q) == 0 and oranges > 0:
            return -1
        if len(q) == 0:
            return 0
        # bfs
        while q:
            cur_row, cur_col, time = q.popleft()
            # print(cur_row, cur_col, time)
            next_steps = self.get_next_steps(cur_row, cur_col, grid)
            for row, col in next_steps:
                # print(row, col)
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    q.append([row, col, time+1])
                    # print(f"bg:{bg}")
                    bg = max(bg, time+1)
                    # print(f"bg:{bg}")
        # Checking to make sure every row and col has been seen
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col] == 1:
                    return -1 
        return bg
    def record_seen(self, row, col):
        if row not in self.seen:
            self.seen[row] = set()
        self.seen[row].add(col)
    def been_seen(self, row, col):
        return row in self.seen and col in self.seen[row]
    def get_num_cells_seen(self):
        cells = 0
        for row in self.seen:
            cells += len(self.seen[row])
        return cells
    def get_next_steps(self, cur_row, cur_col, grid):
        next_steps = []
        steps = [[-1, 0],[0, 1],[1, 0],[0, -1]]
        for change_row, change_col in steps:
            row = cur_row + change_row
            col = cur_col + change_col
            # Checking if in range
            if row < 0 or row >= self.rows:
                continue
            if col < 0 or col >= self.cols:
                continue
            if self.been_seen(row, col):
                continue
            if grid[row][col] == 1:
                next_steps.append([row, col])
            self.record_seen(row, col)
        return next_steps
