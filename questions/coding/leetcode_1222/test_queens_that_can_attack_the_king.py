from questions.coding.leetcode_1222.queens_that_can_attack_the_king import Solution

import pytest

@pytest.mark.parametrize('queens, king, expected', [
    ([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0], [[0,1],[1,0],[3,3]]),
    ([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3], [[2,2],[3,4],[4,4]]),
    ([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4], [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]),
    ([[1,1],[1,2],[1,3],[1,4],[1,5],[2,1],[2,2],[2,3],[2,4],[2,5],[3,1],[3,2],[3,4],[3,5],[4,1],[4,2],[4,3],[4,4],[4,5],[5,1],[5,2],[5,3],[5,4],[5,5]], [3,3], [[2,2],[2,3],[2,4],[3,2],[3,4],[4,2],[4,3],[4,4]]),
])
def test_queensAttacktheKing(queens, king, expected):
    sol = Solution()

    got = sol.queensAttacktheKing(queens, king)
    got = sorted(got)
    expected = sorted(expected)
    assert got == expected
