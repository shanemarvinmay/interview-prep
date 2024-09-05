class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        dp = []
        for row in range(rows):
            dp.append([])
            for col in range(cols):
                if row == 0 or col == 0:
                    dp[-1].append(1)
                else:
                    dp[-1].append(0)
        
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        
        return dp[-1][-1]

'''

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
'''