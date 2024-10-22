from typing import List

# Attempt 0 (Better for interviews)
# class Solution:
#     def findDiagonalOrder(self, m: List[List[int]]) -> List[int]:
#         output = []
#         # Getting max cols
#         max_cols = 0
#         for row in m:
#             max_cols = max(len(row), max_cols)
#         # Getting diagonals from each row, from the first col
#         for start_row in range(0, len(m)-1):
#             row = start_row
#             col = 0
#             while row >= 0 and col <= max_cols:
#                 if col < len(m[row]):
#                     output.append(m[row][col])
#                 row -= 1
#                 col += 1
#         # Taking care of the diagonals on the bottom row.
#         for start_col in range(max_cols):
#             col = start_col
#             row = len(m) - 1
#             while row >= 0 and col <= max_cols:
#                 if col < len(m[row]):
#                     output.append(m[row][col])
#                 row -= 1
#                 col += 1
#         return output

# Attempt 1
class Solution:
    def findDiagonalOrder(self, m: List[List[int]]) -> List[int]:
        output = []
        diagonal_map = dict()
        max_key = 0
        for row in range(len(m)-1, -1, -1):
            for col in range(len(m[row])):
                key = row + col
                max_key = max(key, max_key)
                if key not in diagonal_map:
                    diagonal_map[key] = []
                diagonal_map[key].append(m[row][col])
        for i in range(max_key+1):
            output.extend(diagonal_map[i])
        return output
'''
1424. Diagonal Traverse II
https://leetcode.com/problems/diagonal-traverse-ii/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=MEDIUM%2CHARD&status=TO_DO
'''