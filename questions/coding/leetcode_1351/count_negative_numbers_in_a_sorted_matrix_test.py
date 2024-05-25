from count_negative_numbers_in_a_sorted_matrix_solution import Solution

import pytest

@pytest.mark.parametrize('grid, expected', [
    ([[4,3,2,-1],
      [3,2,1,-1],
      [1,1,-1,-2],
      [-1,-1,-2,-3]], 8),
    ([[3,2],
      [1,0]], 0)
])
def test_count_negatives(grid, expected):
    solution = Solution()

    assert solution.countNegatives(grid) == expected

@pytest.mark.parametrize('nums, expected', [
    ([5,3,1,0,-1,-2], 4),
    ([-1, -2, -3], 0),
    ([3,2,1], -1)
])
def test_binary_search_for_first_neg(nums, expected):
    solution = Solution()

    assert solution.binary_search_for_first_neg(nums) == expected 