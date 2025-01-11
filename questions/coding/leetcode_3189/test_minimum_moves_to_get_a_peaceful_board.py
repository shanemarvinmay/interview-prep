from questions.coding.leetcode_3189.minimum_moves_to_get_a_peaceful_board import Solution

import pytest

@pytest.mark.parametrize('rooks, expected', [
    ([[0,0],[1,0],[1,1]], 3),
    ([[0,0],[0,1],[0,2],[0,3]], 6),
    ([[0,0],[3,2],[1,2],[3,0],[3,4]], 4),
    ([[0,1],[3,2],[1,4],[0,2],[3,4]], 6),
])
def test_minMoves(rooks, expected):
    sol = Solution()

    got = sol.minMoves(rooks)

    assert got == expected
