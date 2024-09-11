from questions.coding.leetcode_624.maximum_distance_in_arrays import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

# @pytest.mark.parametrize('ars, expected', [
#     ([[1,2,3],[4,5],[1,2,3]], 4),
#     ([[1],[1]], 0)
# ])
# def test_maxDistance(ars, expected, sol):
#     got = sol.maxDistance(ars)

#     assert got == expected
