from questions.coding.leetcode_1638.count_substrings_that_differ_by_one_character import Solution

import pytest

@pytest.mark.parametrize('s, t, expected', [
    ("aba", "baba", 6),
    ("ab", "bb", 3)
])
def test_countSubstrings(s, t, expected):
    sol = Solution()

    got = sol.countSubstrings(s, t)

    assert got == expected
