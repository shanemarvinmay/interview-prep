from typing import List

import pytest

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        islands = 0
        self.m == matrix
        for row in range(len(self.m)):
            for col in range(len(self.m[row])):
                if self.m[row][col]:
                    islands += self.get_island_count(row, col)
        return islands
    def get_island_count(self, start_x, start_y) -> int:
        end_x, end_y = start_x, start_y
        stack = [(start_x, start_y)]
        while stack:
            nxt = []
            while stack:
                x, y = stack.pop()
                self.m[x][y] = 0
                right = self.right(x, y)
                down = self.down(x, y)
                diagonal = self.diagonal(x, y)
                if diagonal and down and right:
                    end_x += 1
                    end_y += 1
                    nxt.append((x+1,y+1))
                    nxt.append((x+1,y))
                    nxt.append((x,y+1))
                elif down:
                    end_x += 1
                    nxt.append((x+1,y))
                elif right:
                    end_y += 1
                    nxt.append((x,y+1))
            stack = nxt
        # Getting iland count
        island_count = 0
        area = (end_y - start_y) * (end_x * start_x)
        i = 1
        while i*i <= area:
            island_count += area // i*i
        return island_count
    def right(self, x, y):
        in_range = x < len(self.m) and y+1 < len(self.m[x])
        return in_range and self.m[x][y+1]
    def down(self, x, y):
        in_range = x+1 < len(self.m)
        return in_range and self.m[x+1][y]
    def diagonal(self, x, y):
        in_range = x+1 < len(self.m) and y+1 < len(self.m[x])
        return in_range and self.m[x+1][y+1]

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
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
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