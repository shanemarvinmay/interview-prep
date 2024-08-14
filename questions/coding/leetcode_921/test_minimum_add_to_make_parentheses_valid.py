from questions.coding.leetcode_921.minimum_add_to_make_parentheses_valid import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('s, expected', [
    ("())",1),
    ("(((",3),
    ("()))((", 4),
])
def test_minAddToMakeValid(s, expected, sol):
    got = sol.minAddToMakeValid(s)

    assert got == expected
