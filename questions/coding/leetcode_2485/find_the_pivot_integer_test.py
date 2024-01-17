from find_the_pivot_integer_solution import Solution

import pytest

@pytest.fixture()
def pivot_integer():
    s = Solution()
    return s.pivotInteger

# There is a solution
def test_pivot_integer_solution(pivot_integer):
    assert pivot_integer(8) == 6

# There is no solution
def test_pivot_integer_no_solution(pivot_integer):
    assert pivot_integer(4) == -1