from questions.coding.leetcode_59.spiral_matrix_ii import Solution

import pytest

@pytest.mark.parametrize('n, expected', [
    (
        3,
        [
            [1,2,3],
            [8,9,4],
            [7,6,5]
        ]
    ),
    (1, [[1]]),
])
def test_generateMatrix(n, expected):
    sol = Solution()

    got = sol.generateMatrix(n)

    assert got == expected
