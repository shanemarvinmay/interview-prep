from merge_strings_alternately_solution import Solution

import pytest


@pytest.mark.parametrize('word1, word2, expected, message', [
    ('abc', '123', 'a1b2c3', 'Words have equal length'),
    ('abc', '1', 'a1bc', 'First word is longer.'),
    ('a', '123', 'a123', 'Second word is longer.')
])
def test_merger_alernately(word1, word2, expected, message):
    solution = Solution()

    assert solution.mergeAlternately(word1, word2) == expected, message