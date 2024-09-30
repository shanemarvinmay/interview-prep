from questions.coding.leetcode_1318.minimum_flips_to_make_a_or_b_equal_to_c import Solution

import pytest

@pytest.mark.parametrize('a, b, c, expected', [
    (2, 6, 5, 3),
    (0, 1, 3, 1),
    (0, 3, 0, 2),
])
def test_minFlips(a, b, c, expected):
    sol = Solution()

    got = sol.minFlips(a, b, c)

    assert got == expected
