from questions.coding.leetcode_701.insert_into_a_binary_search_tree import Solution, TreeNode
from questions.coding.util.util import assert_binary_trees_are_equal

from copy import deepcopy
import pytest

@pytest.fixture()
def tree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root

@pytest.fixture()
def expected(tree):
    root = deepcopy(tree)
    root.right.left = TreeNode(5)
    return root


def test_insertIntoBST(tree, expected):
    sol = Solution()
    val = 5
    
    got = sol.insertIntoBST(tree, val)

    assert_binary_trees_are_equal(got, expected)
