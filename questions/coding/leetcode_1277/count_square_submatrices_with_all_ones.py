from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        box_count = dict()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    continue
                neighbors = self.get_neighbors(matrix, row, col)
                if len(neighbors) == 3:
                    matrix[row][col] += min(neighbors)
                val = matrix[row][col]
                while val:
                    if val not in box_count:
                        box_count[val] = 0
                    box_count[val] += 1
                    val -= 1
        total = 0
        for _, count in box_count.items():
            total += count
        return total
    def get_neighbors(self, matrix, row, col):
        neighbors = []
        # Top
        if row > 0:
            neighbors.append(matrix[row-1][col])
        # Diagonal left
        if row > 0 and col > 0:
            neighbors.append(matrix[row-1][col-1])
        # Left
        if col > 0:
            neighbors.append(matrix[row][col-1])
        return neighbors
