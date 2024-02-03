from number_of_common_factors_solution import Solution

import pytest

@pytest.mark.parametrize('a, b, expected, message', [
    (3, 7, 1, 'No factors (besides 1), prime numbers.'),
    (12, 6, 4, 'Multiple factors, one number is a factor of the other.')
])
def test_common_factors(a, b, expected, message):
    solution = Solution()

    assert solution.commonFactors(a, b) == expected, message