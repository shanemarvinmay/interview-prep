from questions.coding.leetcode_841.keys_and_rooms import Solution

import pytest


@pytest.mark.parametrize('rooms, expected', [
    ([[1],[2],[3],[]], True),
    ([[1,3],[3,0,1],[2],[0]],False),
])
def test_canVisitAllRooms(rooms, expected):
    sol = Solution()

    got = sol.canVisitAllRooms(rooms)

    assert got == expected
