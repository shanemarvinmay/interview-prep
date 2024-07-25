from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        self.land = land
        self.farms = []
        self.row, self.col = 0, 0
        while self.row < len(self.land):
            self.col = 0
            while self.col < len(self.land[self.row]):
                top_corner = self.find_next_farm()
                if top_corner[0] == -1:
                    return self.farms
                botttom_corner = self.find_end_of_farm(top_corner)
                self.farms.append([
                    top_corner[0],
                    top_corner[1],
                    botttom_corner[0],
                    botttom_corner[1]
                ])
                # Erasing farm we just captured.
                for row in range(top_corner[0], botttom_corner[0] + 1):
                    for col in range(top_corner[1], botttom_corner[1] + 1):
                        self.land[row][col] = 0
                self.row = top_corner[0]
                self.col += 1
            self.row += 1
        return self.farms
    
    def find_next_farm(self):
        while self.row < len(self.land):
            if self.col >= len(self.land[self.row]):
                self.col = 0
            while self.col < len(self.land[self.row]):
                if self.land[self.row][self.col] == 1:
                    return [self.row, self.col]
                self.col += 1
            self.row += 1
        return [-1, -1] # No farm found.

    def find_end_of_farm(self, top_corner):
        self.row, self.col = top_corner
        while self.col < len(self.land[self.row]) and self.land[self.row][self.col] != 0:
            self.col += 1
        self.col -= 1
        while self.row < len(self.land) and self.land[self.row][self.col] != 0:
            self.row += 1
        self.row -= 1

        return [self.row, self.col]
