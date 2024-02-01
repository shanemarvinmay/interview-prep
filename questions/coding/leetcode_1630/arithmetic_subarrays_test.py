from arithmetic_subarrays_solution import Solution

import pytest

@pytest.mark.parametrize('nums, l, r, expected', [
    ([4,6,5,9,3,7], [0,0,2], [2,3,5], [True, False, True]),
    ([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], [0,1,6,4,8,7], [4,4,9,7,9,10], [False,True,False,False,True,True]),
    ([-3,-6,-8,-4,-2,-8,-6,0,0,0,0], [5,4,3,2,4,7,6,1,7], [6,5,6,3,7,10,7,4,10], [True,True,True,True,False,True,True,True,True])
])
def test_check_arithmetic_subarrays(nums, l, r, expected):
    solution = Solution()

    assert solution.checkArithmeticSubarrays(nums, l, r) == expected