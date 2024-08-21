from questions.coding.leetcode_3195.find_the_minimum_area_to_cover_all_ones_i import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('grid, expected', [
    # ([[0,1,0],[1,0,1]], 6),
    # ([[1,0],[0,0]], 1),
    # ([[0],[1]], 1),
    ([[0,0,0],[0,0,0],[0,0,0],[1,0,1]], 3)
])
def test_minimumArea(grid, expected, sol):
    got = sol.minimumArea(grid)

    assert got == expected
