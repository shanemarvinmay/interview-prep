from typing import List

import pytest

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        islands = 0
        self.m = matrix
        self.dp = [[-1 for _ in range(len(self.m[0]))] for _ in range(len(self.m))]
        for row in range(len(self.m)):
            for col in range(len(self.m[row])):
                if self.m[row][col]:
                    islands += self.get_island_count(row, col)
        return islands
    def get_island_count(self, x, y) -> int:
        if x >= len(self.m) or y >= len(self.m[0]): return 0
        if self.m[x][y] == 0: return 0
        if self.dp[x][y] != -1: return self.dp[x][y]
        right = self.get_island_count(x, y+1)
        diagonal = self.get_island_count(x+1, y+1)
        down = self.get_island_count(x+1, y)
        self.dp[x][y] = min([right, diagonal, down]) + 1
        return self.dp[x][y]

@pytest.mark.parametrize('m, expected', [
    ([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
], 15),
([
  [1,0,1],
  [1,1,0],
  [1,1,0]
], 7)
])
def test_countSquares(m, expected):
    sol = Solution()

    got = sol.countSquares(m)

    assert got == expected

@pytest.mark.parametrize('m, expected', [
    ([
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ], 14)
])
def test_get_island_count(m, expected):
    sol = Solution()
    sol.m = m

    got = sol.get_island_count(0,0)

    assert got == expected

'''
1277. Count Square Submatrices with All Ones
* turn visited to 0 so no double count
* get num islands
    * i = 1
    * while i*i < area:
        islands += area // i*i
        i += 1
* dfs on islands
    * strtx, strty
    * if diagonal and down: endx ++
    * if right: endy ++
    * 

Input: matrix =

Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 

Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

 

Constraints:

    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1

'''