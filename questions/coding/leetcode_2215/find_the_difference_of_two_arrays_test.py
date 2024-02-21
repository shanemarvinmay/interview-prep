from find_the_difference_of_two_arrays_solution import Solution

import pytest


@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1,2,3], [2,4,6], [[1,3],[4,6]]),
    ([1,2,3,3], [1,1,2,2], [[3],[]]),
    ([-80,-15,-81,-28,-61,63,14,-45,-35,-10], 
     [-1,-40,-44,41,10,-43,69,10,2],
     [[-81,-35,-10,-28,-61,-45,-15,14,-80,63],[-1,2,69,-40,41,10,-43,-44]])
])
def test_find_difference(nums1, nums2, expected):
    solution = Solution()

    got = solution.findDifference(nums1, nums2)
    got[0].sort()
    got[1].sort()
    expected[0].sort()
    expected[1].sort()

    assert got == expected
