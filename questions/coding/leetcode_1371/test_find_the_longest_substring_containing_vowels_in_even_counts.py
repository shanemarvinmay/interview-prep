from questions.coding.leetcode_1371.find_the_longest_substring_containing_vowels_in_even_counts import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ("eleetminicoworoep", 13),
    ("leetcodeisgreat", 5),
    ("bcbcbc", 6),
    ("axeeioooou", 4),
])
def test_findTheLongestSubstring(s, expected):
    sol = Solution()

    got = sol.findTheLongestSubstring(s)

    assert got == expected
