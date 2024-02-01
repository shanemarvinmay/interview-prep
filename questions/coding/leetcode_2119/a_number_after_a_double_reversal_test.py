from a_number_after_a_double_reversal_solution import Solution

import pytest

@pytest.mark.parametrize('num, expected', [(526, True), (1800, False), (0, True)])
def test_is_same_after_reversals(num, expected):
    solution = Solution()

    assert solution.isSameAfterReversals(num) == expected