from typing import List
from collections import deque

class Solution:
    def slidingPuzzle(self, b: List[List[int]]) -> int:
        if self.is_solved(b):
            return 0
        self.min_moves = float('inf')
        rows = len(b)
        cols = len(b[0])
        self.seen = set([self.serialize(b)])

        # Finding where 0 starts
        x = y = 0
        for row in range(rows):
            for col in range(cols):
                if b[row][col] == 0:
                    x = row
                    y = col
                    break

        pos_moves = deque(self.get_moves(b, x, y, move_count=1))
        while pos_moves:
            b, x, y, move_count = pos_moves.popleft()
            
            if self.is_solved(b):
                self.min_moves = min(self.min_moves, move_count)
            pos_moves.extend(self.get_moves(b, x, y, move_count+1))

        if self.min_moves != float('inf'):
            return self.min_moves
        return -1

    def serialize(self, b):
        return f"{','.join(str(num) for num in b[0])},{','.join(str(num) for num in b[1])}"
    def get_moves(self, b, x, y, move_count):
        moves = []
        if move_count > self.min_moves: return moves
        steps = [[-1,0], [0,1], [1,0], [0,-1]]
        for change_x, change_y in steps:
            new_x = x + change_x
            new_y = y + change_y
            if new_x < 0 or new_x >= len(b) or new_y < 0 or new_y >= len(b[0]):
                continue
            new_b = [row[:] for row in b]
            new_b[x][y], new_b[new_x][new_y] = new_b[new_x][new_y], new_b[x][y]
            serialized_b = self.serialize(new_b)
            if serialized_b in self.seen: continue
            self.seen.add(serialized_b)
            moves.append([new_b, new_x, new_y, move_count])
        return moves
    def is_solved(self, b):
        return self.serialize(b) == '1,2,3,4,5,0'