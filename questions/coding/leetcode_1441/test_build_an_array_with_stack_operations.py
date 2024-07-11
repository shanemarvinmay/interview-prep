from questions.coding.leetcode_1441.build_an_array_with_stack_operations import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('target, n, expected', [
    ([1,3], 3, ["Push","Push","Pop","Push"]),
    ([1,2,3], 3, ["Push","Push","Push"]),
    ([1,2], 4, ["Push","Push"]),
])
def test_buildArray(target, n, expected, sol):
    got = sol.buildArray(target, n)

    assert got == expected
