from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.islands = 0
        '''
        blow up graph
        / -> 1 1 0
             1 0 1
             0 1 1'''
        m = self.blow_up(grid)
        # Count the islands
        self.map_islands(m)
        return self.islands
    def blow_up(self, grid):
        # making matrix
        m = []
        for row in range(len(grid)*3):
            new_row = []
            for col in range(len(grid[0])*3):
                new_row.append(1)
            m.append(new_row)
        # making dashes
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                _row, _col = row * 3, col * 3
                if grid[row][col] == '\\':
                    m[_row][_col] = 0
                    m[_row+1][_col+1] = 0
                    m[_row+2][_col+2] = 0
                elif grid[row][col] == '/':
                    m[_row][_col+2] = 0
                    m[_row+1][_col+1] = 0
                    m[_row+2][_col] = 0 
        return m
    def map_islands(self, m):
        for row in range(len(m)):
            for col in range(len(m[row])):
                # Checking/mapping if we found an island.
                if m[row][col]:
                    self.islands += 1
                    self.map_island(m, row, col)
                # Marking spot as 'visited' if it's an island.
                m[row][col] = 0
                
    def map_island(self, m, row, col):
        m[row][col] = 0
        # up
        if row > 0 and m[row-1][col] == 1:
            self.map_island(m, row-1, col)
        # down
        if row + 1 < len(m) and m[row+1][col] == 1:
            self.map_island(m, row+1, col)
        # left
        if col > 0 and m[row][col-1] == 1:
            self.map_island(m, row, col-1)
        # right
        if col + 1 < len(m[row]) and m[row][col+1] == 1:
            self.map_island(m, row, col+1)
