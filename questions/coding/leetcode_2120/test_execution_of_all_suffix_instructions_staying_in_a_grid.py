from questions.coding.leetcode_2120.execution_of_all_suffix_instructions_staying_in_a_grid import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('n, start_pos, moves, expected', [
    (3, [0,1], "RRDDLU", [1,5,4,3,1,0]),
    (2, [1,1], "LURD", [4,1,0,0]),
    (1, [0,0], "LRUD", [0,0,0,0]),
])
def test_executeInstructions(n, start_pos, moves, expected, sol):
    got = sol.executeInstructions(n, start_pos, moves)

    assert got == expected
