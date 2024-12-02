from typing import List
import heapq

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1 
        rows = len(grid)
        cols = len(grid[0])
        heap = [[0,0,0]]
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def get_next_steps(cur_time, row, col):
            next_steps = []
            pos_steps = [[-1,0], [0,1], [1,0], [0,-1]]
            for change_row, change_col in pos_steps:
                r = row + change_row
                c = col + change_col
                if 0<=r<rows and 0<=c<cols and not visited[r][c]:
                    gap = grid[r][c] - cur_time
                    wait_time = 1 if gap % 2 == 0 else 0
                    time = max(grid[r][c]+ wait_time, cur_time + 1)
                    next_steps.append([time, r, c])
            return next_steps
        while heap:
            cur_time, row, col = heapq.heappop(heap)
            if visited[row][col]: continue
            visited[row][col] = True
            if row == rows-1 and col == cols-1:
                return cur_time
            next_steps = get_next_steps(cur_time, row, col)
            while next_steps:
                time, r, c = next_steps.pop()
                if visited[r][c]: continue
                heapq.heappush(heap, [time, r, c])
