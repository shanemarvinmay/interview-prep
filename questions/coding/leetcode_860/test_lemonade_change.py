from questions.coding.leetcode_860.lemonade_change import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('bills, expected', [
    # ([5,5,5,10,20], True),
    ([5,5,10,10,20], False),
    # ([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5], True),
])
def test_lemonadeChange(bills, expected, sol):
    got = sol.lemonadeChange(bills)

    assert got == expected
