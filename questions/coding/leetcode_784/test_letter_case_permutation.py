from questions.coding.leetcode_784.letter_case_permutation import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('s, expected', [
    ("a1b2", ["a1b2","A1b2","a1B2","A1B2"]),
    ("3z4", ["3Z4","3z4"]),
    ('123', ['123']),
    ('C', ['c','C'])
])
def test_letterCasePermutation(s, expected, sol):
    got = sol.letterCasePermutation(s)
    for i in got:
        assert i in expected
    for i in expected:
        assert i in got
