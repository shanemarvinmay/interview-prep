from questions.coding.leetcode_1529.minimum_suffix_flips import Solution

import pytest

@pytest.mark.parametrize('target, expected', [
    ("10111", 3),
    ("101", 3),
    ("00000",  0),
    ("001011101", 5),
])
def test_minFlips(target, expected):
    sol = Solution()

    got = sol.minFlips(target)

    assert got == expected
