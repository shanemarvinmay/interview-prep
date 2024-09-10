from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        # {row :{col}}
        self.seen = dict()
        bg = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.seen_it(row, col): continue
                if self.grid[row][col]:
                    sz = self.get_island_size(row, col)
                    bg = max(bg, sz)
                else:
                    self.record(row, col)
        return bg
    def get_island_size(self, row, col):
        sz = 0
        moves = [(row, col)]
        while moves:
            row, col = moves.pop()
            if self.seen_it(row, col): continue
            self.record(row, col)
            sz += 1
            # up
            if self.is_in_range(row-1, col) and self.grid[row-1][col]:
                moves.append((row-1,col))
            # down
            if self.is_in_range(row+1, col) and self.grid[row+1][col]:
                moves.append((row+1, col))
            # left
            if self.is_in_range(row, col-1) and self.grid[row][col-1]:
                moves.append((row, col-1))
            # right
            if self.is_in_range(row, col+1) and self.grid[row][col+1]:
                moves.append((row, col+1))
        return sz
    def is_in_range(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])
    def record(self, row, col):
        if row not in self.seen:
            self.seen[row] = set()
        self.seen[row].add(col)
    def seen_it(self, row, col):
        return col in self.seen.get(row, set())      

'''
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
'''