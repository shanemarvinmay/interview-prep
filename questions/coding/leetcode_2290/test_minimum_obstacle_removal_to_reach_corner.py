from questions.coding.leetcode_2290.minimum_obstacle_removal_to_reach_corner import Solution

import pytest

@pytest.mark.parametrize('grid, expected', [
    ([[0,1,1],[1,1,0],[1,1,0]], 2),
    ([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 0),
])
def test_minimumObstacles(grid, expected):
    sol = Solution()

    got = sol.minimumObstacles(grid)

    assert got == expected
