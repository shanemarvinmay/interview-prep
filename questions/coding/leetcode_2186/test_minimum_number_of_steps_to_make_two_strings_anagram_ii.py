from questions.coding.leetcode_2186.minimum_number_of_steps_to_make_two_strings_anagram_ii import Solution

import pytest


@pytest.mark.parametrize('s, t, expected', [
    ("leetcode", "coats", 7),
    ("night", "thing", 0),
    ('aaa', 'a', 2),
])
def test_minSteps(s, t, expected):
    sol = Solution()

    got = sol.minSteps(s, t)

    assert got == expected
