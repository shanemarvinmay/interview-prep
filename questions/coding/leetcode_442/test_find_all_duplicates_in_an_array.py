from questions.coding.leetcode_442.find_all_duplicates_in_an_array import Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('nums, expected', [
    ([4,3,2,7,8,2,3,1], [2,3]),
    ([1], []),
    ([10,2,5,10,9,1,1,4,3,7], [1, 10]),
])
def test_findDuplicates(nums, expected, sol):
    got = sol.findDuplicates(nums)

    assert got == expected
