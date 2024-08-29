from questions.coding.leetcode_1448.count_good_nodes_in_binary_tree import Solution
from questions.coding.util.util import list_to_binary_tree

import pytest

@pytest.mark.parametrize('root, expected', [
    (list_to_binary_tree([3,1,4,3,None,1,5]), 4),
    (list_to_binary_tree([3,3,None,4,2]), 3),
    (list_to_binary_tree([1]), 1),
])
def test_goodNodes(root, expected):
    sol = Solution()

    got = sol.goodNodes(root)

    assert got == expected
