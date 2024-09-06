from questions.coding.leetcode_1884.egg_drop_with_2_eggs_and_n_floors import Solution

import pytest


@pytest.mark.parametrize('n, expected', [
    (2, 2),
    (100, 14),
])
def test_twoEggDrop(n, expected):
    sol = Solution()

    got = sol.twoEggDrop(n)

    assert got == expected
