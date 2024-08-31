from questions.coding.leetcode_1701.average_waiting_time import Solution

import pytest

@pytest.mark.parametrize('customers, exepcted', [
    ([[1,2],[2,5],[4,3]], 5),
    ([[5,2],[5,4],[10,3],[20,1]], 3.25),
])
def test_averageWaitingTime(customers, exepcted):
    sol = Solution()

    got = sol.averageWaitingTime(customers)

    assert got == exepcted
