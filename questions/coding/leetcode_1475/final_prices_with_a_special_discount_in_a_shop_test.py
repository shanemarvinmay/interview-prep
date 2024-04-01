from final_prices_with_a_special_discount_in_a_shop_solution import Solution

import pytest

@pytest.mark.parametrize('prices, expected', [
    ([8,4,6,2,3], [4,2,4,2,3]),
    ([1,2,3,4,5], [1,2,3,4,5])
])
def test_final_prices(prices, expected):
    solution = Solution()

    assert solution.finalPrices(prices) == expected