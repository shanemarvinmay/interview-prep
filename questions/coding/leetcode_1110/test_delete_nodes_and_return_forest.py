from questions.coding.leetcode_1110.delete_nodes_and_return_forest import Solution, TreeNode
from questions.coding.util.util import assert_binary_trees_are_equal, list_to_binary_tree

import pytest

@pytest.mark.parametrize('root, targets, expected', [
    ([1,2,3,4,5,6,7], [3,5], [[1,2,None,4],[6],[7]]),
    ([1,2,4,None,3],[3], [[1,2,4]]),
    ([1,2,None,4,3], [2,3], [[1],[4]]),
    ([1,2,3,None,None,None,4], [2,1], [[3,None,4]]),
    ([1,2,3,None,None,None,4], [2,1], [[3,None,4]]),
])
def test_delNodes(root, targets, expected):
    sol = Solution()
    root = list_to_binary_tree(root)

    got = sol.delNodes(root, targets)

    for i in range(len(expected)):
        tree = list_to_binary_tree(expected[i])

        assert_binary_trees_are_equal(got[i], tree)
