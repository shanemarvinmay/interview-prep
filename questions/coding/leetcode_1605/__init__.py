from questions.coding.leetcode_1605.find_valid_matrix_given_row_and_column_sums import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

def test_init_matrix(sol):
    expected = [
        [3, 5],
        [6, 7]
    ]
    row_sums = [3, 8]
    col_sums = [4, 7]
    
    sol.init_matrix()
    got = sol.matrix

    assert got == expected