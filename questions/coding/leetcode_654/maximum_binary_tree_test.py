from maximum_binary_tree_solution import *

# import pytest

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
    if root1.right and root2.right:
        # print('Right')
        assert_binary_trees_are_equal(root1.right, root2.right)

# @pytest.mark.parametrize('input_list', [(), ([3, 2, 1])])
def test_construct_maximum_binary_tree_normal_tree():
    input_list = [3, 2, 1, 6, 0, 5]
    expected = TreeNode(6)
    expected.left = TreeNode(3)
    expected.right = TreeNode(5)
    expected.left.right = TreeNode(2)
    expected.right.left = TreeNode(0)
    expected.left.right.right = TreeNode(1)
    solution = Solution()

    got = solution.constructMaximumBinaryTree(input_list)

    assert_binary_trees_are_equal(got, expected)

def test_construct_maximum_binary_tree_empty_tree():
    solution = Solution()

    assert solution.constructMaximumBinaryTree([]) is None
