from questions.coding.leetcode_1823.find_the_winner_of_the_circular_game import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def test_cases():
    n_k_expected = {
        1: {
            1:1,
        },
        2: {
            1:2,
            2:1,
        },
        3: {
            1:3,
            2:3,
            3:2,
        },
        4: {
            1:4,
            2:1,
            3:1,
            4:2
        },
    }
    return n_k_expected

def test_findTheWinner(sol, test_cases):
    for n in test_cases:
        for k in test_cases[n]:
            got = sol.findTheWinner(n, k)
            expected = test_cases[n][k]
            assert got == expected
