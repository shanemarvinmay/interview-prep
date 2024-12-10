from questions.coding.leetcode_2981.find_longest_special_substring_that_occurs_thrice_i import Solution

import pytest

@pytest.mark.parametrize('s, expected', [
    ('aaaa', 2),
    ('abcdef', -1),
    ('abcaba', 1),
])
def test_maximumLength(s, expected):
    sol = Solution()

    got = sol.maximumLength(s)

    assert got == expected
