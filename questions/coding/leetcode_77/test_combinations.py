from questions.coding.leetcode_77.combinations import Solution

import pytest

@pytest.mark.parametrize('n, r, expected', [
    (4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
    (1, 1,  [[1]]),
])
def test_combine(n, r, expected):
    sol = Solution()

    got = sol.combine(n, r)

    assert got == expected
