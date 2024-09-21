from questions.coding.leetcode_1850.minimum_adjacent_swaps_to_reach_the_kth_smallest_number import Solution

import pytest

@pytest.mark.parametrize('num, expected', [
    ('5142', '5214'),
    ('5214', '5241'),
    ('5412', '5421'),
])
def test_get_next_permutation(num, expected):
    sol = Solution()

    got = sol.get_next_permutation(num)
    got = ''.join(got)

    assert got == expected

@pytest.mark.parametrize('num, k, expected', [
    ('5489355142', 4, 2),
    ('11112', 4, 4),
    ('00123', 1, 1),
])
def test_getMinSwaps(num, k, expected):
    sol = Solution()

    got = sol.getMinSwaps(num, k)

    assert got == expected
