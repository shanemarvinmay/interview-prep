from typing import List

class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        min_moves = 0
        n = len(rooks)
        rows = [0] * n
        cols = [0] * n

        # Populating how many rooks are in each row and col
        for row, col in rooks:
            rows[row] += 1
            cols[col] += 1
        
        # Calc moves
        cur_pieces_to_move_row = 0
        cur_pieces_to_move_col = 0
        for i in range(n):
            # Putting -1 here b/c we want 1 in each row and col
            cur_pieces_to_move_row += rows[i] - 1
            cur_pieces_to_move_col += cols[i] - 1
            # abs is used here because there might be pieces we are cur missing
            # so the cur pieces might be negative
            min_moves += abs(cur_pieces_to_move_row) + abs(cur_pieces_to_move_col)
        
        return min_moves

