from number_of_rectangles_that_can_form_the_largest_square_solution import Solution

import pytest

@pytest.mark.parametrize('rectangles, expected', [
    ([[5,8],[3,9],[5,12],[16,5]], 3),
    ([[2,3],[3,7],[4,3],[3,7]], 3)
])
def test_count_good_rectangles(rectangles, expected):
    solution = Solution()

    assert solution.countGoodRectangles(rectangles) == expected
