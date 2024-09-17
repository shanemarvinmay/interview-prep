from questions.coding.leetcode_1706.where_will_the_ball_fall import Solution

import pytest

@pytest.mark.parametrize('grid, expected', [
    (
        [
            [1,1,1,-1,-1],
            [1,1,1,-1,-1],
            [-1,-1,-1,1,1],
            [1,1,1,1,-1],
            [-1,-1,-1,-1,-1]
        ],
        [1,-1,-1,-1,-1]
    ),
    ([[-1]], [-1]),
    (
        [
            [1,1,1,1,1,1],
            [-1,-1,-1,-1,-1,-1],
            [1,1,1,1,1,1],
            [-1,-1,-1,-1,-1,-1]
        ],
        [0,1,2,3,4,-1]
    ),
])
def test_findBall(grid, expected):
    sol = Solution()

    got = sol.findBall(grid)

    assert got == expected
