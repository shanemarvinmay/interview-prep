from questions.coding.leetcode_3239.minimum_number_of_flips_to_make_binary_grid_palindromic_i import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('grid, expected', [
    ([[1,0,0],[0,0,0],[0,0,1]], 2),
    ([[0,1],[0,1],[0,0]], 1),
    ([[1],[0]], 0),
])
def test_minFlips(grid, expected, sol):
    got = sol.minFlips(grid)

    assert got == expected
