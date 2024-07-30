from questions.coding.leetcode_1043.partition_array_for_maximum_sum import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()
'''
Constraints:
1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
'''
@pytest.mark.parametrize('ar, k, expected', [
    ([1,15,7,9,2,5,10], 3, 84),
    ([1,4,1,5,7,3,6,1,9,9,3], 4, 83),
    ([1], 1, 1),
])
def test_maxSumAfterPartitioning(ar, k, expected, sol):
    got = sol.maxSumAfterPartitioning(ar, k)

    assert got == expected
