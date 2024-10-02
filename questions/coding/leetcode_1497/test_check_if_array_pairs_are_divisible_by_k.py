from questions.coding.leetcode_1497.check_if_array_pairs_are_divisible_by_k import Solution

import pytest

@pytest.mark.parametrize('ar, k, expected', [
    # Leetcode examples testcases.
    ([1,2,3,4,5,10,6,7,8,9], 5, True),
    ([1,2,3,4,5,6], 7, True),
    ([1,2,3,4,5,6], 10, False),
    # match: neg, zero, pos
    ([-1,0,0,2,2,3], 2, True),
    # no match: neg, zero, pos
    ([-1,0,2,2], 2, False),
    # no match because of 3 nums need eachother
    ([0,2,2,-1], 2, False),
    # test case I missed in leetcode submission
    ([-4,-7,5,2,9,1,10,4,-8,-3], 3, True),
])
def test_canArrange(ar, k, expected):
    sol = Solution()

    got = sol.canArrange(ar, k)

    assert got == expected
