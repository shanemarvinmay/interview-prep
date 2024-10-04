from questions.coding.leetcode_1249.minimum_remove_to_make_valid_parentheses import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ("lee(t(c)o)de)", "lee(t(c)o)de"),
    ("a)b(c)d", "ab(c)d"),
    ("))((", ""),
    ("l(ov)e", "l(ov)e"),
])
def test_minRemoveToMakeValid(s, expected):
    sol = Solution()

    got = sol.minRemoveToMakeValid(s)

    assert got == expected
