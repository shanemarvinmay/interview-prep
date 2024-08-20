from questions.coding.leetcode_1743.restore_the_array_from_adjacent_pairs import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('adj_pairs, expected', [
    ([[2,1],[3,4],[3,2]],[1,2,3,4]),
    ([[4,-2],[1,4],[-3,1]], [-2,4,1,-3]),
    ([[100000,-100000]], [100000,-100000])
])
def test_restoreArray(adj_pairs, expected, sol):
    got = sol.restoreArray(adj_pairs)

    assert got == expected