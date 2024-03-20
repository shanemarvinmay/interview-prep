class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter_to_col_num = {
            'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8
        }
        # If both the row and col are odd
        # or both are even, then the color is black
        row = int(coordinates[1])
        col = letter_to_col_num[coordinates[0]]

        both_even = row % 2 == 0 and col % 2 == 0
        both_odd = row % 2 and col % 2

        if both_even or both_odd:
            return False
        
        return True