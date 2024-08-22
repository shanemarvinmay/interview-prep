from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        num_bars = 0
        costs.sort()
        i = 0
        while i < len(costs) and costs[i] <= coins:
            num_bars += 1
            coins -= costs[i]
            i += 1
        return num_bars

'''
Input: costs = 
Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.
Example 2:

Input: costs = [10,6,8,7,7,8], coins = 5, 0
Explanation: The boy cannot afford any of the ice cream bars.
Example 3:

Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6
Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.
'''