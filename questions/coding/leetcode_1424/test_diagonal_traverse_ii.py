from questions.coding.leetcode_1424.diagonal_traverse_ii import Solution

import pytest

@pytest.mark.parametrize('m, expected', [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,4,2,7,5,3,8,6,9]),
    ([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]], [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]),
])
def test_findDiagonalOrder(m, expected):
    sol = Solution()

    got = sol.findDiagonalOrder(m)

    assert got == expected

'''
Constraints:
1 <= nums.length <= 105
1 <= nums[i].length <= 105
1 <= sum(nums[i].length) <= 105
1 <= nums[i][j] <= 105
'''