from calculate_money_in_leetcode_bank_solution import Solution

import pytest

@pytest.mark.parametrize('num_days, expected', [
    (4, 10), (10, 37), (20, 96)
])
def test_total_money(num_days, expected):
    solution = Solution()

    assert solution.totalMoney(num_days) == expected
