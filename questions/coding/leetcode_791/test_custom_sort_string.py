from questions.coding.leetcode_791.custom_sort_string import Solution

import pytest

@pytest.mark.parametrize('order, s, expected', [
    ("ce", "deca", "ceda"),
    ("bcafg", "abcd", 'bcad'),
    ("cba", "abcd", 'cbad'),
])
def test_customSortString(order, s, expected):
    sol = Solution()

    got = sol.customSortString(order, s)

    assert got == expected
