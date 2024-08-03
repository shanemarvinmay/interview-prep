from questions.coding.leetcode_419.battleships_in_a_board import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

def test_countBattleships(sol):
    expected = 2
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

    got = sol.countBattleships(board)

    assert got == expected
