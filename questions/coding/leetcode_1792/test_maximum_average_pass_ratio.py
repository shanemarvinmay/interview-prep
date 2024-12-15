from questions.coding.leetcode_1792.maximum_average_pass_ratio import Solution

import pytest

@pytest.mark.parametrize('classes, extra, expected', [
    ([[1,2],[3,5],[2,2]], 2, 0.78333),
    ([[2,4],[3,9],[4,5],[2,10]], 4, 0.53485),
])
def test_maxAverageRatio(classes, extra, expected):
    sol = Solution()

    got = sol.maxAverageRatio(classes, extra) * 100
    got = round(got, 2)

    assert got == round(expected * 100, 2)

