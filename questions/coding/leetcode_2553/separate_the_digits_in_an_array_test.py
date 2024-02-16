from separate_the_digits_in_an_array_solution import Solution

import pytest

@pytest.mark.parametrize('nums, expected', [
    ([13,25,83,77], [1,3,2,5,8,3,7,7]),
    ([7,1,3,9], [7,1,3,9])
    ])
def test_separate_digits(nums, expected):
    solution = Solution()

    assert solution.separateDigits(nums) == expected