from questions.coding.leetcode_3271.hash_divided_string import Solution

import pytest

@pytest.mark.parametrize('s, k, expected', [
    ("abcd", 2, "bf"),
    ("mxz", 3,"i"),
])
def test_stringHash(s, k, expected):
    sol = Solution()

    got = sol.stringHash(s, k)

    assert got == expected
