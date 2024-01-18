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

''' The original solution found when lower_sum == higher_sum, then took the
average of low and high (if it was a round number). This worked for the above
examples but failed for 15. So this is to ensure the new solution works.
(It does. So don't break it!)
'''
def test_pivot_integer_no_mid_solution(pivot_integer):
    assert pivot_integer(15) == -1