from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        coord = [rStart, cStart]
        self.path = [coord[:]]
        self.rows, self.cols = rows, cols
        jump_length = 0
        while len(self.path) < rows * cols:
            jump_length += 1
            # right
            coord = self.go_next_coord(coord, jump_length, 'right')
            # down
            coord = self.go_next_coord(coord, jump_length, 'down')
            jump_length += 1
            # left
            coord = self.go_next_coord(coord, jump_length, 'left')
            # up
            coord = self.go_next_coord(coord, jump_length, 'up')
            
        return self.path
    def is_in_range(self, coord):
        return  0 <= coord[0] < self.rows and 0 <= coord[1] < self.cols
    def go_next_coord(self, coord, jump_length, direction):
        start = coord[:]
        if direction == 'up':
            coord[0] -= jump_length
        elif direction == 'right':
            coord[1] += jump_length
        elif direction == 'down':
            coord[0] += jump_length
        else:
            coord[1] -= jump_length
        if start[0] < coord[0] or start[1] < coord[1]:
            step=1
        else:
            step=-1
        for row in range(start[0], coord[0] + step, step):
            for col in range(start[1], coord[1] + step, step):
                if self.is_in_range([row, col]) and [row,col] != self.path[-1]:
                    self.path.append([row,col])

        return coord
