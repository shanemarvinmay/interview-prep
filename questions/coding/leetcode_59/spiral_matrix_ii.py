from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = self.get_base_matrix(n)
        num = 1
        row = 0
        col = -1
        while True:
            # Right
            col += 1
            while col < len(m[row]):
                # Ran into a spot already filled by a number.
                if m[row][col]:
                    break
                m[row][col] = num
                num += 1
                col += 1
            col -= 1
            # Down
            row += 1
            while row < len(m):
                # Ran into a spot already filled by a number.
                if m[row][col]:
                    break
                m[row][col] = num
                num += 1
                row += 1
            row -= 1
            # Left
            col -= 1
            while col >= 0:
                # Ran into a spot already filled by a number.
                if m[row][col]:
                    break
                m[row][col] = num
                num += 1
                col -= 1
            col += 1
            # Up
            row -= 1
            while row >= 0:
                # Ran into a spot already filled by a number.
                if m[row][col]:
                    break
                m[row][col] = num
                num += 1
                row -= 1
            row += 1
            if self.check_if_at_end_of_m(m, row, col): 
                break
        return m
    def check_if_at_end_of_m(self, m, row, col):
        if m[row][col] == 0:
            return False
        # right
        if col + 1 < len(m[0]) and m[row][col + 1] == 0:
            return False
        # down
        if row + 1 < len(m) and m[row+1][col] == 0:
            return False
        # left
        if col - 1 >= 0 and m[row][col-1] == 0:
            return False
        # up
        if row - 1 >= 0 and m[row-1][col] == 0:
            return False
        return True
    def get_base_matrix(self, n):
        m = []
        for i in range(n):
            m.append([])
            for j in range(n):
                m[-1].append(0)
        return m
