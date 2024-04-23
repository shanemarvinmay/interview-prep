from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_count = 0

        # Attempt 1 O(row * log(col))
        for row in range(len(grid) - 1, -1, -1):
            # Do binary search to find first neg
            first_neg_idx = self.binary_search_for_first_neg(grid[row])
            if first_neg_idx != -1:
                negative_count += len(grid[row]) - first_neg_idx

        # Attempt 0 O(row * col)
        # for row in range(len(grid) - 1, -1, -1):
        #     # Do binary search to find first neg
        #     # If no neg, return -1
        #     for col in range(len(grid[row]) - 1, -1, -1):
        #         if grid[row][col] >= 0:
        #             break
        #         negative_count += 1
        
        return negative_count
    
    def binary_search_for_first_neg(self, row):
        l = 0
        r = len(row) - 1

        while l <= r:
            m = (l + r) // 2
            # If positive, go right
            if row[m] >= 0:
                l = m + 1
            # If negative
            else:
                # Check if first neg and return idx.
                if m == 0 or row[m-1] >= 0:
                    return m
                # Need to go left.
                else:
                    r = m - 1
        # No negative was found.
        return -1
