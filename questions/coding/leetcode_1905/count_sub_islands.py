from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        subislands = 0
        # {row: {col, col}}
        self.locations = dict()
        self.num_rows = len(grid1)
        self.num_cols = len(grid2[0]) # Guarenteed grid will have >= 1 rows.
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.seen(row, col): continue
                if grid2[row][col] and self.is_subisland(row, col, grid1, grid2):
                    subislands += 1
                else:
                    self.record_location(row, col)
        return subislands
    def is_subisland(self, row, col, grid1, grid2):
        moves = [(row, col)]
        is_subisland = grid1[row][col] == 1
        while moves:
            row, col = moves.pop()
            if self.seen(row, col): continue
            self.record_location(row, col)
            # Up 1.
            if self.is_in_range(row -1, col) and grid2[row-1][col]:
                if grid1[row-1][col] == 0:
                    is_subisland = False
                moves.append((row-1, col))
            # Right 1.
            if self.is_in_range(row, col+1) and grid2[row][col+1]:
                if grid1[row][col+1] == 0:
                    is_subisland = False
                moves.append((row, col+1))
            # Down 1.
            if self.is_in_range(row + 1, col) and grid2[row+1][col]:
                if grid1[row+1][col] == 0:
                    is_subisland = False
                moves.append((row+1, col))
            # Left 1.
            if self.is_in_range(row, col-1) and grid2[row][col-1]:
                if grid1[row][col-1] == 0:
                    is_subisland = False
                moves.append((row, col-1))

        return is_subisland
    def seen(self, row, col):
        return row in self.locations and col in self.locations[row]
    def record_location(self, row, col):
        if row not in self.locations:
            self.locations[row] = set()
        self.locations[row].add(col)
    def is_in_range(self, row=0, col=0):
        if row < 0 or row >= self.num_rows:
            return False
        elif col < 0 or col >= self.num_cols:
            return False
        return True
