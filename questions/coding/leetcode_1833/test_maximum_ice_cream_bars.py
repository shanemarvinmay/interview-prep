from questions.coding.leetcode_1833.maximum_ice_cream_bars import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('costs, coins, expected', [
    ([1,3,2,4,1], 7,4),
    ([10,6,8,7,7,8], 5, 0),
    ([1,6,3,1,2,5], 20, 6),
])
def test_maxIceCream(costs, coins, expected, sol):
    got = sol.maxIceCream(costs, coins)

    assert got == expected
