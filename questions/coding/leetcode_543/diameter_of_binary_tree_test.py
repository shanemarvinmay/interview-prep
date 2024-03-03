from diameter_of_binary_tree_solution import Solution

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
      1
    /   
   2
 /
3
'''
one_path_tree = TreeNode(1)
one_path_tree.left = TreeNode(2)
one_path_tree.left.left = TreeNode(3)
'''
    1
    /\
   2  3
  /  \
 4    5
  \   /
   6 7
  /   \
 8     9
'''
longest_path_not_thru_root = TreeNode(1)
longest_path_not_thru_root.left = TreeNode(2)
longest_path_not_thru_root.right = TreeNode(3)
longest_path_not_thru_root.left.left = TreeNode(4)
longest_path_not_thru_root.left.right = TreeNode(5)
longest_path_not_thru_root.left.left.right = TreeNode(6)
longest_path_not_thru_root.left.right.left = TreeNode(7)
longest_path_not_thru_root.left.left.right.left = TreeNode(8)
longest_path_not_thru_root.left.right.left.right = TreeNode(9)
'''
     1
    / \
   2   3
  /     \
 4       5
'''
two_path_tree = TreeNode(1)
two_path_tree.left = TreeNode(2)
two_path_tree.right = TreeNode(3)
two_path_tree.left.left = TreeNode(4)
two_path_tree.right.right = TreeNode(5)


@pytest.mark.parametrize('binary_tree, expected', [
    (one_path_tree, 2),
    (two_path_tree, 4),
    (longest_path_not_thru_root, 6)
])
def test_diameter_of_binary_tree(binary_tree, expected):
    solution = Solution()

    got = solution.diameterOfBinaryTree(binary_tree)

    assert got == expected