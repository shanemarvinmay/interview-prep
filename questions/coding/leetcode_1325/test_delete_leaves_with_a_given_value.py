from questions.coding.leetcode_1325.delete_leaves_with_a_given_value import Solution, TreeNode
from questions.coding.util.util import assert_binary_trees_are_equal

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def tree_of_targets():
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    return root

@pytest.fixture()
def tree_with_some_targets(tree_of_targets):
    tree_of_targets.left.left = TreeNode(2)
    tree_of_targets.right = TreeNode(3)
    tree_of_targets.right.left = TreeNode(2)
    tree_of_targets.right.right = TreeNode(4)
    return tree_of_targets

@pytest.fixture()
def expected_tree_without_targets():
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    return root

@pytest.mark.parametrize('tree, target, expected', [
    ('tree_of_targets', 2, None),
    ('tree_with_some_targets', 2, 'expected_tree_without_targets'),
])
def test_removeLeafNodes(tree, target, expected, request, sol):
    tree = request.getfixturevalue(tree)
    expected = request.getfixturevalue(expected) if isinstance(expected, str) else expected

    got = sol.removeLeafNodes(tree, target)

    assert_binary_trees_are_equal(got, expected)