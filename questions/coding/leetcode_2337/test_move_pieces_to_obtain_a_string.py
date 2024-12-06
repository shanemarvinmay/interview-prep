from questions.coding.leetcode_2337.move_pieces_to_obtain_a_string import Solution

import pytest

@pytest.mark.parametrize('s, t, expected', [
    ('_L__R__R_', 'L______RR', True),
    ('R_L_', '__LR', False),
    ('_RL_', 'R__L', False),
])
def test_canChange(s, t, expected):
    sol = Solution()

    got = sol.canChange(s,t)

    assert got == expected
