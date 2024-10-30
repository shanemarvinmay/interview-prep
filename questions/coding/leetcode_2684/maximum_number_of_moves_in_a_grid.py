from typing import List

class Solution:
    def maxMoves(self, m: List[List[int]]) -> int:
        rows = len(m)
        cols = len(m[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for c in range(cols-2, -1, -1):
            for r in range(rows):
                moves = [-1]
                if r-1>=0 and m[r-1][c+1] > m[r][c]:
                    moves.append(dp[r-1][c+1])
                if m[r][c+1] > m[r][c]:
                    moves.append(dp[r][c+1])
                if r+1<rows and m[r+1][c+1] > m[r][c]:
                    moves.append(dp[r+1][c+1])
                dp[r][c] = max(moves)+1
        
        # Get max from first col of dp
        bg = 0
        for row in dp:
            bg = max(bg, row[0])
        
        return bg