from merge_two_binary_trees_solution import Solution

import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def assert_binary_trees_are_equal(root1, root2):
    '''This function asserts 2 binary trees have the same shape and vals.'''
    # Either both roots must be None or both must exist
    assert (root1 is None and root2 is None) or (root1 and root2)
    if root1 is None and root2 is None:
        return
    # Roots have same val.
    # print(root1.val, root2.val)
    assert root1.val == root2.val
    # Roots both have lefts or both do not have lefts.
    assert (root1.left is None and root2.left is None) or (root1.left and root2.left)
    if root1.left and root2.left:
        # print('Left')
        assert_binary_trees_are_equal(root1.left, root2.left)
    # Roots have both have rights both do not have rights.
    assert (root1.right is None and root2.right is None) or (root1.right and root2.right)

@pytest.fixture()
def two_binary_trees_with_some_overlap():
    '''Returns 2 input trees and the expected output tree.'''
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    expected = TreeNode(3)
    expected.left = TreeNode(4)
    expected.right = TreeNode(5)
    expected.left.left = TreeNode(5)
    expected.left.right = TreeNode(4)
    expected.right.right = TreeNode(7)

    return root1, root2, expected

@pytest.fixture()
def root1_empty_root2_full_tree():
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    return None, root2, root2

@pytest.fixture()
def root1_full_root2_empty():
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    return root1, None, root1

@pytest.mark.parametrize('fixture', [
    ('two_binary_trees_with_some_overlap'),
    ('root1_empty_root2_full_tree'),
    ('root1_full_root2_empty')
])
def test_merge_trees(fixture, request):
  solution = Solution()

  root1, root2, expected = request.getfixturevalue(fixture)

  got = solution.mergeTrees(root1, root2)

  assert_binary_trees_are_equal(got, expected)
'''
some overlap some missing from each
   3r
 4  5
5 4   7

   2r
 1  3
  4  7

one tree is empty
1
 2r

1
 2r
'''