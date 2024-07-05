from questions.coding.leetcode_1008.construct_binary_search_tree_from_preorder_traversal import Solution, TreeNode
from questions.coding.util.util import assert_binary_trees_are_equal

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def odd_num_nodes_bst():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    return root

@pytest.fixture()
def even_num_nodes_bst():
    root = TreeNode(3)
    root.left = TreeNode(1)
    return root

@pytest.mark.parametrize('preorder, expected_fixture', [
    ([1,4,3,7,9,8,5], 'odd_num_nodes_bst'),
    ([1,3], 'even_num_nodes_bst'),
])
def test_bstFromPreorder(preorder, expected_fixture, request, sol):
    expected = request.getfixturevalue(expected_fixture)

    got = sol.bstFromPreorder(preorder)

    assert_binary_trees_are_equal(got, expected)
