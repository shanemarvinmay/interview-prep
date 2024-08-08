from questions.coding.leetcode_3016.minimum_number_of_pushes_to_type_word_ii import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('word, expected', [
    ("abcde", 5),
    ("xyzxyzxyzxyz", 12),
    ("aabbccddeeffgghhiiiiii", 24),
])
def test_minimumPushes(word, expected, sol):
    got = sol.minimumPushes(word)

    assert got == expected
