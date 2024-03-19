from increasing_order_search_tree_solution import Solution

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

@pytest.fixture(scope='module')
def input_tree():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root

@pytest.fixture(scope='module')
def expected_tree():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    return root

def assert_trees_are_equal(root, another_root):
    if root is None:
        assert another_root is None
        return
    assert root.val == another_root.val
    assert_trees_are_equal(root.left, another_root.left)
    assert_trees_are_equal(root.right, another_root.right)

def test_increasing_bst(input_tree, expected_tree):
    solution = Solution()

    got = solution.increasingBST(input_tree)

    assert_trees_are_equal(got, expected_tree)