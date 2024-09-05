from questions.coding.leetcode_1806.minimum_number_of_operations_to_reinitialize_a_permutation import Solution

import pytest



@pytest.mark.parametrize('n, expected', [
    (2, 1),
    (4, 2),
    (6, 4),
    (10, 6),
])
def test_reinitializePermutation(n, expected):
    sol = Solution()

    got = sol.reinitializePermutation(n)

    assert got == expected
