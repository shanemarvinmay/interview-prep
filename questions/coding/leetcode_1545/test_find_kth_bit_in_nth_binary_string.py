from questions.coding.leetcode_1545.find_kth_bit_in_nth_binary_string import Solution

import pytest

@pytest.mark.parametrize('n, k, expected', [
    (3, 1, '0'),
    (4, 11, '1'),
])
def test_findKthBit(n, k, expected):
    sol = Solution()

    got = sol.findKthBit(n, k)

    assert got == expected
