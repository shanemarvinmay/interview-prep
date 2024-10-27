from questions.coding.leetcode_951.flip_equivalent_binary_trees import Solution
from questions.coding.util.util import list_to_binary_tree

import pytest

@pytest.mark.parametrize('l1, l2, expected', [
    ([1,2,3,4,5,6,None,None,None,7,8], [1,3,2,None,6,4,5,None,None,None,None,8,7], True),
    ([], [], True),
    ([], [1], False),
    ([1,2,3,4,5,6,None,None,None,7,8], [99,3,2,None,6,4,5,None,None,None,None,8,7], False)
])
def test_flipEquiv(l1, l2, expected):
    sol = Solution()
    n1 = list_to_binary_tree(l1)
    n2 = list_to_binary_tree(l2)

    got = sol.flipEquiv(n1, n2)

    assert got == expected
