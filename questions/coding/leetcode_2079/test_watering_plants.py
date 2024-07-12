from questions.coding.leetcode_2079.watering_plants import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('plants, capacity, expected', [
    ([2,2,3,3], 5, 14),
    ([1,1,1,4,2,3],4, 30),
    ([7,7,7,7,7,7,7], 8, 49),
    ([3,2,4,2,1],6,17)
])
def test_wateringPlants(plants, capacity, expected, sol):
    got = sol.wateringPlants(plants, capacity)

    assert got == expected