from questions.coding.leetcode_22.generate_parentheses import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('n, expected', [
    (3, ["((()))","(()())","(())()","()(())","()()()"]),
    (1,["()"]),
])
def test_generateParenthesis(n, expected, sol):
    got = sol.generateParenthesis(n)

    assert got == expected
