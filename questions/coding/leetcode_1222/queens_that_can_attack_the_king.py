from typing import List
from math import sqrt
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        possible_killer_queens = {
            "t": [-100,-100],
            "tr": [-100,-100],
            "r": [-100,-100],
            "dr": [-100,-100],
            "d": [-100,-100],
            "dl": [-100,-100],
            "l": [-100,-100],
            "tl": [-100,-100],
        }
        for queen in queens:
            # if position is already taken, find out which one is closer
            # Check t d (col)
            if queen[1] == king[1]:
                # t
                if queen[0] < king[0]:
                    possible_killer_queens['t'] = self.pick_which_is_closer(possible_killer_queens['t'], queen, king)
                # d
                else:
                    possible_killer_queens['d'] = self.pick_which_is_closer(possible_killer_queens['d'], queen, king)
            # Check l r (row)
            if queen[0] == king[0]:
                # l
                if queen[1] < king[1]:
                    possible_killer_queens['l'] = self.pick_which_is_closer(possible_killer_queens['l'], queen, king)
                # r
                else:
                    possible_killer_queens['r'] = self.pick_which_is_closer(possible_killer_queens['r'], queen, king)
            # Check Diagonal diff in |y| == |x|
            y_diff = self.get_y_diff(queen, king)
            x_diff = self.get_x_diff(queen, king)
            if abs(y_diff) == abs(x_diff):
                # tr
                if y_diff > 0 and x_diff < 0:
                    possible_killer_queens['tr'] = self.pick_which_is_closer(possible_killer_queens['tr'], queen, king)
                # dr
                elif y_diff > 0 and x_diff > 0:
                    possible_killer_queens['dr'] = self.pick_which_is_closer(possible_killer_queens['dr'], queen, king)
                # dr
                elif y_diff < 0 and x_diff > 0:
                    possible_killer_queens['dl'] = self.pick_which_is_closer(possible_killer_queens['dl'], queen, king)
                # tr
                else:
                    possible_killer_queens['tl'] = self.pick_which_is_closer(possible_killer_queens['tl'], queen, king)

        # Rounding up the 8 possible killer queens.
        killer_queens = []
        for _, queen in possible_killer_queens.items():
            if queen[0] >= 0 and queen[1] >= 0:
                killer_queens.append(queen)

        return killer_queens

    def pick_which_is_closer(self, p1, p2, king):
        diff1 = self.get_y_diff(p1, king)**2 + self.get_x_diff(p1, king)**2
        diff1 = sqrt(diff1)
        diff2 = self.get_y_diff(p2, king)**2 + self.get_x_diff(p2, king)**2
        diff2 = sqrt(diff2)
        if diff1 < diff2:
            return p1
        return p2

    def get_x_diff(self, p1, p2):
        '''Returns the difference in rows (x)'''
        return p1[0] - p2[0]
    def get_y_diff(self, p1, p2):
        '''Returns the difference in cols (y)'''
        return p1[1] - p2[1]
