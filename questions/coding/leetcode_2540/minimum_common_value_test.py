from minimum_common_value_solution import Solution

import pytest

@pytest.mark.parametrize('nums1, nums2, expected', [
    ([1,2,3], [2,3], 2),
    ([3,4], [1,2,3,4], 3),
])
def test_get_common(nums1, nums2, expected):
    solution = Solution()

    assert solution.getCommon(nums1, nums2) == expected
