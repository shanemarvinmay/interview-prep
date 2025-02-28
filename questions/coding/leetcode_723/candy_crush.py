from typing import List
from collections import deque

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        crushed = True
        ROWS, COLS = len(board), len(board[0])
        def bfs(r, c):
            if r == 6 and c == 1:
                pass
            crushed = False
            q = deque([(r, c)])
            crush = set()
            while q:
                r, c = q.popleft()
                # Check down
                i = 1
                crush_count = 1
                while 0 <= r + i < ROWS:
                    if (r+i,c) in crush:
                        i += 1 
                        continue
                    if board[r+i][c] == board[r][c]:
                        crush_count += 1
                    elif board[r+i][c] > 0 and board[r+i][c] != board[r][c]:
                        break
                    i += 1
                i -= 1
                if crush_count >= 3:
                    crushed = True
                    for j in range(r+1, r+i+1):
                        if board[r+j][c] < 0: continue
                        q.append((r+j,c))
                        crush.add((r+j, c))
                # Check up
                i = 1
                crush_count = 1
                while 0 <= r - i < ROWS:
                    if (r-i,c) in crush:
                        i += 1 
                        continue
                    if board[r-i][c] == board[r][c]:
                        crush_count += 1
                    elif board[r-i][c] > 0 and board[r-i][c] != board[r][c]:
                        break
                    i += 1
                i -= 1
                if crush_count >= 3:
                    crushed = True
                    for j in range(r-1, r-i-1, -1):
                        if board[r-j][c] < 0: continue
                        q.append((r-j,c))
                        crush.add((r-j, c))
                
                if crushed:
                    crush.add((r,c))
            # Doing the crushing
            for r, c in crush:
                board[r][c] *= -1
            # Dropping
            for _, c in crush:
                i = ROWS - 1
                while i > -1 and board[i][c] > 0: i -= 1
                j = i - 1
                while j > -1:
                    board[i][c], board[j][c] = board[j][c], board[i][c]
                    i -= 1
                    j -= 1

            return crushed
                    
        while crushed:
            crushed = False
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] < 0:
                        continue
                    crushed = crushed or bfs(r, c)
        
        # TODO: drop all crushed
        return board