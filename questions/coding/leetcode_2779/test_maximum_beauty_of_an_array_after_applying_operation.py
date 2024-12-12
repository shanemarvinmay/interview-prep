from questions.coding.leetcode_2779.maximum_beauty_of_an_array_after_applying_operation import Solution

import pytest

@pytest.mark.parametrize('nums, k, expected', [
    ([4,6,1,2], 2, 3),
    ([1,1,1,1], 10, 4),
    ([1,2,3,4], 0, 1),
    ([1,1,2,9_900,10_000,10_100, 10_001], 100, 4),
])
def test_maximumBeauty(nums, k, expected):
    sol = Solution()

    got = sol.maximumBeauty(nums, k)

    assert got == expected
