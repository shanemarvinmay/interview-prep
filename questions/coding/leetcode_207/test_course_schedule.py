from questions.coding.leetcode_207.course_schedule import Solution

import pytest

@pytest.mark.parametrize('num_courses, prereqs, expected', [
    (2, [[1,0]], True),
    (2, [[1,0],[0,1]], False),
    (3, [[0,1],[0,2],[1,2]], True),
    (4, [[1,0]], True),
    (1, [], True),
    (7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]], True),
])
def test_canFinish(num_courses, prereqs, expected):
    sol = Solution()

    got = sol.canFinish(num_courses, prereqs)

    assert got == expected
