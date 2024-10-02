from questions.coding.leetcode_287.find_the_duplicate_number import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([1,3,4,2,2], 2),
    ([3,1,3,4,2], 3),
    ([3,3,3,3,3], 3),
])
def test_findDuplicate(nums, expected):
    sol = Solution()

    got = sol.findDuplicate(nums)

    assert got == expected
