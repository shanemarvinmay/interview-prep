from questions.coding.leetcode_1817.finding_the_users_active_minutes import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('logs, k, expected', [
    ([[0,5],[1,2],[0,2],[0,5],[1,3]], 5, [0,2,0,0,0]),
    ([[1,1],[2,2],[2,3]], 4, [1,1,0,0])
])
def test_findingUsersActiveMinutes(logs, k, expected, sol):
    got = sol.findingUsersActiveMinutes(logs, k)

    assert got == expected