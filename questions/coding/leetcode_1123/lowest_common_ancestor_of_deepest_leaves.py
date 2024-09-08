from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        _, lowest_ancestor = self.helper(root)
        return lowest_ancestor
    def helper(self, root):
        if root is None: return 0, None
        left_height, left_lowest_ancestor = self.helper(root.left)
        right_height, right_lowest_ancestor = self.helper(root.right)
        if left_height > right_height: return left_height + 1, left_lowest_ancestor
        if left_height < right_height: return right_height + 1, right_lowest_ancestor
        # If the heights are equal.
        # Or if we are at a child node (both left and right height = 0).
        return left_height + 1, root
