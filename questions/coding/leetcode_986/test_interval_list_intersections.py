from questions.coding.leetcode_986.interval_list_intersections import Solution

import pytest


@pytest.mark.parametrize('first, second, expected', [
    ([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]], [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]),
    ([[1,3],[5,9]], [], []),
    ([[4,11]], [[1,2],[8,11],[12,13],[14,15],[17,19]], [[8, 11]]),
    ([[3,5],[9,20]], [[4,5],[7,10],[11,12],[14,15],[16,20]], [[4,5],[9,10],[11,12],[14,15],[16,20]]),
])
def test_intervalIntersection(first, second, expected):
    sol = Solution()

    got = sol.intervalIntersection(first, second)

    assert got == expected
