from typing import List
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        heap = [[grid[0][0], 0, 0]]
        heapq.heapify(heap)
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        visited[0][0] = True
        def get_next_steps(row, col):
            next_steps = []
            possible_steps = [[-1,0], [0,1], [1,0], [0,-1]]
            for change_row, change_col in possible_steps:
                r = row + change_row
                c = col + change_col
                if 0<=r<rows and 0<=c<cols and visited[r][c] == False:
                    visited[r][c] = True
                    next_steps.append([grid[r][c], r, c])
            return next_steps
        while heap:
            cur_cost, row, col = heapq.heappop(heap)
            if row == rows-1 and col == cols-1:
                return cur_cost
            next_steps = get_next_steps(row, col)
            for cost, r, c in next_steps:
                heapq.heappush(heap, [cost+cur_cost, r, c])
