from determine_color_of_a_chessboard_square_solution import Solution

import pytest

@pytest.mark.parametrize('coordinate, expected', [
    ("a1", False),
    ("h3", True),
    ('c7', False)
])
def test_square_is_white(coordinate, expected):
    solution = Solution()

    assert solution.squareIsWhite(coordinate) == expected
