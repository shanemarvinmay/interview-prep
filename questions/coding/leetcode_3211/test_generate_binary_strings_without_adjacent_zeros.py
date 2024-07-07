from questions.coding.leetcode_3211.generate_binary_strings_without_adjacent_zeros import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('n, expected', [
    (1, ['0','1']),
    (3, ["010","011","101","110","111"]),
])
def test_validStrings(n, expected, sol):
    got = sol.validStrings(n)

    assert got == expected
