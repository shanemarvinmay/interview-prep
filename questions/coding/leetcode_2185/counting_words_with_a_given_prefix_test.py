from counting_words_with_a_given_prefix_solution import Solution

import pytest

@pytest.mark.parametrize('words, pref, expected', [
    (["pay","attention","practice","attend"], 'at', 2),
    (["leetcode","win","loops","success"], "code", 0)
])
def test_prefix_count(words, pref, expected):
    solution = Solution()

    assert solution.prefixCount(words, pref) == expected