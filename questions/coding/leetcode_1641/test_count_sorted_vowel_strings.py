from questions.coding.leetcode_1641.count_sorted_vowel_strings import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('n, expected', [
    (1, 5),
    (2, 15),
    (33, 66_045),
])
def test_countVowelStrings(n, expected, sol):
    got = sol.countVowelStrings(n)

    assert got == expected