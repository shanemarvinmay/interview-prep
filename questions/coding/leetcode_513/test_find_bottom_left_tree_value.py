from questions.coding.leetcode_513.find_bottom_left_tree_value import Solution
from questions.coding.util.util import list_to_binary_tree

import pytest

@pytest.mark.parametrize('tree_list, expected', [
    ([2,1,3], 1),
    ([1,2,3,4,None,5,6,None,None,7], 7),
    ([ 50, 25, 75, 2, None, 55, None, None, 5, None, 59, 4, 6, 58, None, None, None, None, 7, 57, None ], 7),
])
def test_findBottomLeftValue(tree_list, expected):
    sol = Solution()
    root = list_to_binary_tree(tree_list)

    got = sol.findBottomLeftValue(root)

    assert got == expected
