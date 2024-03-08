from count_elements_with_maximum_frequency_solution import Solution

import pytest


@pytest.mark.parametrize('nums, expected', [
    ([1,2,2,3,1,4], 4),
    ([1,2,3,4,5], 5),
    ([1,2,2,3,3,3,4,4,4], 6)
])
def test_max_frequency_elements(nums, expected):
    solution = Solution()

    assert solution.maxFrequencyElements(nums) == expected