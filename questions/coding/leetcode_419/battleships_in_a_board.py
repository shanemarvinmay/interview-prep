from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ship_count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'X':
                    ship_count += 1
                    self.sink_ship(board, row, col)
        return ship_count
    
    def sink_ship(self, board, row, col):
        # Verticle ship.
        if row < len(board)-1 and board[row+1][col] == 'X':
            while row < len(board) and board[row][col] == 'X':
                board[row][col] = '.'
                row += 1
        # Horizontal ship.
        else:
            while col < len(board[row]) and board[row][col] == 'X':
                board[row][col] = '.'
                col += 1
