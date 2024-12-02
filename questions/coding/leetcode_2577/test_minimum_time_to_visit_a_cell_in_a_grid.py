from questions.coding.leetcode_2577.minimum_time_to_visit_a_cell_in_a_grid import Solution

import pytest

@pytest.mark.parametrize('grid, expected', [
    ([[0,1,3,2],[5,1,2,5],[4,3,8,6]], 7),
    ([[0,2,4],[3,2,1],[1,0,4]], -1),
    ([
        [0,1,1,1,1],
        [1,9,1,9,1],
        [1,1,1,9,1]
    ], 6),
    ([
        [0,1],
        [3,5],
        [18,9]
    ], 9)
])
def test_minimumTime(grid, expected):
    sol = Solution()

    got = sol.minimumTime(grid)

    assert got == expected
