from questions.coding.leetcode_1992.find_all_groups_of_farmland import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('land, expected', [
    ([[1,0,0],[0,1,1],[0,1,1]], [[0,0,0,0],[1,1,2,2]]),
    ([[1,1],[1,1]], [[0,0,1,1]]),
    ([[0]], []),
    ([[1,1,0,0,0,1],[1,1,0,0,0,0]], [[0,0,1,1],[0,5,0,5]])
])
def test_findFarmland(land, expected, sol):
    got = sol.findFarmland(land)

    assert got == expected
