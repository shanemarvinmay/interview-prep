from questions.coding.leetcode_1861.rotating_the_box import Solution

import pytest

@pytest.mark.parametrize('box, expected', [
    ([["#",".","#"]],
    [
    ["."],
    ["#"],
    ["#"]]),
    ([
    ["#",".","*","."],
    ["#","#","*","."]],
    [
    ["#","."],
    ["#","#"],
    ["*","*"],
    [".","."]]),
    ([
    ["#","#","*",".","*","."],
    ["#","#","#","*",".","."],
    ["#","#","#",".","#","."]],
    [
    [".","#","#"],
    [".","#","#"],
    ["#","#","*"],
    ["#","*","."],
    ["#",".","*"],
    ["#",".","."]]),

])
def test_rotateTheBox(box, expected):
    sol = Solution()

    got = sol.rotateTheBox(box)

    assert got == expected
