from difference_between_ones_and_zeros_in_row_and_column_solution import Solution

import pytest

@pytest.fixture()
def mixed_square_matrix():
    grid = [
        [0,1,1],
        [1,0,1],
        [0,0,1]
        ]
    difference = [
        [0,0,4],
        [0,0,4],
        [-2,-2,2]
        ]
    return grid, difference

@pytest.fixture()
def only_ones_rect_matrix():
    grid = [
        [1,1,1],
        [1,1,1]
        ]
    difference = [
       [5,5,5],
       [5,5,5]
        ]
    return grid, difference

@pytest.fixture()
def only_zeros_rect_matrix():
    grid = [
        [0, 0, 0],
        [0, 0, 0]
        ]
    difference = [
       [-5,-5,-5],
       [-5,-5,-5]
        ]
    return grid, difference

@pytest.mark.parametrize('fixture_case, message', [
    ('mixed_square_matrix', 'Mixed square matrix.'),
    ('only_ones_rect_matrix', 'Only ones rect matrix.'),
    ('only_zeros_rect_matrix', 'Only zeros rect matrix.'),
])
def test_ones_minus_zeros(fixture_case, message, request):
    solution = Solution()
    grid, expected = request.getfixturevalue(fixture_case)

    assert solution.onesMinusZeros(grid) == expected, message