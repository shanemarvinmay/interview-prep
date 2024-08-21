from questions.coding.leetcode_2294.partition_array_such_that_maximum_difference_is_k import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, k, expected', [
    ([3,6,1,2,5], 2, 2),
    ([1,2,3], 1, 2),
    ([2,2,4,5], 0, 3),
    ([1,2,3], 4, 1),
])
def test_partitionArray(nums, k, expected, sol):
    got = sol.partitionArray(nums, k)

    assert got == expected
