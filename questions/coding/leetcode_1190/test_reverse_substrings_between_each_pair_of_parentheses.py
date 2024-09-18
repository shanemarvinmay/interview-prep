from questions.coding.leetcode_1190.reverse_substrings_between_each_pair_of_parentheses import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ("(abcd)","dcba"),
    ("(u(love)i)", "iloveu"),
    ("(ed(et(oc))el)", "leetcode"),
    ("a(bcdefghijkl(mno)p)q", "apmnolkjihgfedcbq"),
    ('a(b(cde)f(ghi)j)k', 'ajghifcdebk'),
])
def test_reverseParentheses(s, expected):
    sol = Solution()

    got = sol.reverseParentheses(s)

    assert got == expected
