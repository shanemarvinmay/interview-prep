from questions.coding.leetcode_695.max_area_of_island import Solution

import pytest

@pytest.mark.parametrize('grid, expected', [
    ([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ], 6),
    ([[0,0,0,0,0,0,0,0]], 0),
])
def test_maxAreaOfIsland(grid, expected):
    sol = Solution()

    got = sol.maxAreaOfIsland(grid)

    assert got == expected
