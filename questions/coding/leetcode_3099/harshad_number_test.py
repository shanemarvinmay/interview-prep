from harshad_number_solution import Solution

import pytest

@pytest.mark.parametrize('num, expected', [
    (18, 9),
    (23, -1)
])
def test_sum_of_the_digits_of_harshad_number(num, expected):
    solution = Solution()

    assert solution.sumOfTheDigitsOfHarshadNumber(num) == expected
