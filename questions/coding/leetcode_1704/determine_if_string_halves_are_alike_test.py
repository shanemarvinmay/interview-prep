from determine_if_string_halves_are_alike_solution import Solution

import pytest

@pytest.mark.parametrize('s, expected', [("book", True), ("textbook", False)])
def test_halves_are_alike(s, expected):
    solution = Solution()

    assert solution.halvesAreAlike(s) == expected