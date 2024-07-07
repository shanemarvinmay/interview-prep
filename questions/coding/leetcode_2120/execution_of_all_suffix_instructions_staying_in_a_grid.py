from typing import List

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], moves: str) -> List[int]:
        output = []

        for i in range(len(moves)):
            move_count = 0
            coord = Coord(startPos[0], startPos[1])
            for j in range(i, len(moves)):
                coord = self.move(moves[j], coord)
                if self.is_valid(n, coord):
                    move_count += 1
                else:
                    break
            output.append(move_count)
        
        return output

    def move(self, direction, start):
        if direction == 'U':
            return Coord(start.x-1, start.y)
        elif direction == 'R':
            return Coord(start.x, start.y+1)
        elif direction == 'D':
            return Coord(start.x+1, start.y)
        else:
            return Coord(start.x, start.y-1)

    def is_valid(self, n, coord):
        lower_bounds = coord.x >= 0 and coord.y >= 0
        upper_bounds = coord.x < n and coord.y < n
        return lower_bounds and upper_bounds
