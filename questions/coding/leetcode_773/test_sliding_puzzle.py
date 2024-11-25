from questions.coding.leetcode_773.sliding_puzzle import Solution

import pytest

@pytest.mark.parametrize('board, expected', [
    ([[1,2,3],[4,0,5]], 1),
    ([[4,1,2],[5,0,3]], 5),
    ([[1,2,3],[5,4,0]], -1),
    ([[1,2,3],[4,5,0]], 0),
])
def test_slidingPuzzle(board, expected):
    sol = Solution()

    got = sol.slidingPuzzle(board)

    assert got == expected
