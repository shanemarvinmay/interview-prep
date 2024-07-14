from questions.coding.leetcode_3075.maximize_happiness_of_selected_children import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('happiness, kids, expected', [
    ([1,2,3], 2, 4),
    ([1,1,1,1], 2, 1),
    ([2,3,4,5], 1, 5),
])
def test_maximumHappinessSum(happiness, kids, expected, sol):
    got = sol.maximumHappinessSum(happiness, kids)

    assert got == expected
