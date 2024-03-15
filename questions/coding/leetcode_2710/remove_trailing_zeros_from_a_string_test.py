from remove_trailing_zeros_from_a_string_solution import Solution

import pytest

@pytest.mark.parametrize('num, expected', [
    ("51230100", "512301"),
    ("123", "123")
])
def test_remove_trailing_zeros(num, expected):
    solution = Solution()

    assert solution.removeTrailingZeros(num) == expected
