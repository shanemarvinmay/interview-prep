from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        heights = [0] * num_cols

        for row in range(num_rows):
            # Updating heights.
            for col in range(num_cols):
                if matrix[row][col]:
                    heights[col] += 1
                else:
                    heights[col] = 0
            # Checking current areas.
            ordered = sorted(heights, reverse=True)
            for i in range(len(ordered)):
                ans = max(ans, ordered[i] * (i+1))
        
        return ans