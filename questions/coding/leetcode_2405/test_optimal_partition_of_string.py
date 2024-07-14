from questions.coding.leetcode_2405.optimal_partition_of_string import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('s, expected', [
    ("abacaba", 4),
    ("ssssss", 6),
])
def test_partitionString(s, expected, sol):
    got = sol.partitionString(s)

    assert got == expected
