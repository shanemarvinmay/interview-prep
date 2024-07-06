from questions.coding.leetcode_2785.sort_vowels_in_a_string import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()
"""
Example 1:

Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
Example 2:

Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
"""
@pytest.mark.parametrize('s, expected', [
   ('lEetcOde', 'lEOtcede'),
   ('lYmpH', 'lYmpH'),
])
def test_sortVowels(s, expected, sol):
    got = sol.sortVowels(s)

    assert got == expected