from questions.coding.leetcode_2640.find_the_score_of_all_prefixes_of_an_array import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([2,3,7,5,10], [4,10,24,36,56]),
    ([1,1,2,4,8,16], [2,4,8,16,32,64]),
])
def test_findPrefixScore(nums, expected):
    sol = Solution()

    got = sol.findPrefixScore(nums)

    assert got == expected
