from questions.coding.leetcode_1072.flip_columns_for_maximum_number_of_equal_rows import Solution

import pytest

@pytest.mark.parametrize('matrix, expected', [
    ([[0,1],[1,1]], 1),
    ([[0,1],[1,0]], 2),
    ([[0,0,0],[0,0,1],[1,1,0]], 2),
])
def test_maxEqualRowsAfterFlips(matrix, expected):
    sol = Solution()

    got = sol.maxEqualRowsAfterFlips(matrix)

    assert got == expected
