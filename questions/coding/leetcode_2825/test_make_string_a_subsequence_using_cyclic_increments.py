from questions.coding.leetcode_2825.make_string_a_subsequence_using_cyclic_increments import Solution

import pytest

@pytest.mark.parametrize('s1, s2, expected', [
    ('abc', 'ad', True),
    ('zc', 'ad', True),
    ('ab', 'd', False),
    ('a', 'ab', False),
    ("eao", "ofa", False),
])
def test_canMakeSubsequence(s1, s2, expected):
    sol = Solution()

    got = sol.canMakeSubsequence(s1, s2)

    assert got == expected