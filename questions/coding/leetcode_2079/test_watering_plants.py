from questions.coding.leetcode_2079.watering_plants import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()
'''
Example 1:
Input: plants = , capacity = 5
Output: 14
Explanation: Start at the river with a full watering can:
- Walk to plant 0 (1 step) and water it. Watering can has 3 units of water.
- Walk to plant 1 (1 step) and water it. Watering can has 1 unit of water.
- Since you cannot completely water plant 2, walk back to the river to refill (2 steps).
- Walk to plant 2 (3 steps) and water it. Watering can has 2 units of water.
- Since you cannot completely water plant 3, walk back to the river to refill (3 steps).
- Walk to plant 3 (4 steps) and water it.
Steps needed = 1 + 1 + 2 + 3 + 3 + 4 = 14.
Example 2:
Input: plants = , capacity = 4
Output: 30
Explanation: Start at the river with a full watering can:
- Water plants 0, 1, and 2 (3 steps). Return to river (3 steps).
- Water plant 3 (4 steps). Return to river (4 steps).
- Water plant 4 (5 steps). Return to river (5 steps).
- Water plant 5 (6 steps).
Steps needed = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30.
Example 3:
Input: plants = [7,7,7,7,7,7,7], capacity = 8
Output: 49
Explanation: You have to refill before watering each plant.
Steps needed = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49.
 

Constraints:
n == plants.length
1 <= n <= 1000
1 <= plants[i] <= 106
max(plants[i]) <= capacity <= 109'''
@pytest.mark.parametrize('plants, capacity, expected', [
    # ([2,2,3,3], 5, 14),
    # ([1,1,1,4,2,3],4, 30),
    # ([7,7,7,7,7,7,7], 8, 49),
    ([3,2,4,2,1],6,17)
])
def test_wateringPlants(plants, capacity, expected, sol):
    got = sol.wateringPlants(plants, capacity)

    assert got == expected