from questions.coding.leetcode_1261.find_elements_in_a_contaminated_binary_tree import TreeNode, FindElements
from questions.coding.util.util import assert_binary_trees_are_equal

import pytest

@pytest.fixture()
def small_perfect_tree():
    root = TreeNode(-1)
    root.left = TreeNode(-1)
    root.right = TreeNode(-1)
    return root

@pytest.fixture()
def expected_small_perfect_tree(small_perfect_tree):
    small_perfect_tree.val = 0
    small_perfect_tree.left.val = 1
    small_perfect_tree.right.val = 2
    return small_perfect_tree

def test_setup_tree(small_perfect_tree, expected_small_perfect_tree):
    find_elements = FindElements(small_perfect_tree)

    got = find_elements.root

    assert_binary_trees_are_equal(got, expected_small_perfect_tree)

