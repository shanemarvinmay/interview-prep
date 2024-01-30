from maximum_number_of_coins_you_can_get_solution import Solution

import pytest

@pytest.mark.parametrize('piles, expected', [
    ([2,4,1,2,7,8], 9),
    ([2,4,5], 4),
    ([9,8,7,6,5,1,2,3,4], 18)
])
def test_max_coins(piles, expected,):
    solution = Solution()

    assert solution.maxCoins(piles) == expected