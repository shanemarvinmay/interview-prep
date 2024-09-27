from questions.coding.leetcode_2711.difference_of_number_of_distinct_values_on_diagonals import Solution

import pytest

@pytest.mark.parametrize('grid, expected', [
    ([[1,2,3],[3,1,5],[3,2,1]], [[1,1,0],[1,0,1],[0,1,1]]),
    ([[1]], [[0]]),
])
def test_differenceOfDistinctValues(grid, expected):
    sol = Solution()

    got = sol.differenceOfDistinctValues(grid)

    assert got == expected
