from questions.coding.leetcode_2486.append_characters_to_string_to_make_subsequence import Solution

import pytest

@pytest.mark.parametrize('s, t, expected', [
    ("coaching", "coding", 4),
    ("abcde", "a", 0),
    ("z", "abcde", 5),
])
def test_appendCharacters(s, t, expected):
    sol = Solution()

    got = sol.appendCharacters(s, t)

    assert got == expected
