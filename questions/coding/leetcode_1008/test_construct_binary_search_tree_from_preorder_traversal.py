from questions.coding.leetcode_1008.construct_binary_search_tree_from_preorder_traversal import Solution, TreeNode
from questions.coding.util.util import assert_binary_trees_are_equal

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def normal_bst():
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(7)
    root.right = TreeNode(10)
    root.right.right = TreeNode(12)
    return root

@pytest.fixture()
def small_bst():
    root = TreeNode(1)
    root.right = TreeNode(3)
    return root

@pytest.mark.parametrize('preorder, expected_fixture', [
    ([8,5,1,7,10,12], 'normal_bst'),
    ([1,3], 'small_bst'),
])
def test_bstFromPreorder(preorder, expected_fixture, request, sol):
    expected = request.getfixturevalue(expected_fixture)

    got = sol.bstFromPreorder(preorder)

    assert_binary_trees_are_equal(got, expected)
