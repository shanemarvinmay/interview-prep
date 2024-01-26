from count_equal_and_divisible_pairs_in_an_array_solution import Solution

import pytest

@pytest.mark.parametrize('nums, k, expected, message', [
    ([3,1,2,2,2,1,3], 2, 4, 'Some pairs qualify and some do not'),
    ([1,2,3], 1, 0, 'No pairs in list.'),
    ([5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3], 7, 18, 'Not sure')
])
def test_count_pairs(nums, k, expected, message):
    solution = Solution()

    assert solution.countPairs(nums, k) == expected, message
