from questions.coding.leetcode_2832.maximal_range_that_each_element_is_maximum_in_it import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([1,5,4,3,6], [1,4,2,1,5]),
    ([96,65,4,5,71,9,48,82,52,62], [10,3,1,2,6,1,2,9,1,2]),
])
def test_maximumLengthOfRanges(nums, expected):
    sol = Solution()

    got = sol.maximumLengthOfRanges(nums)

    assert got == expected
