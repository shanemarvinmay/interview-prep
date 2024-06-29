from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def find_big_diff_for_node(self, root, ancestor, big_diff):
        big_diff = max(big_diff, abs(ancestor - root.val))
        if root.left:
            left_big_diff = self.find_big_diff_for_node(root.left, ancestor, big_diff)
            big_diff = max(big_diff, left_big_diff)
        if root.right:
            right_big_diff = self.find_big_diff_for_node(root.right, ancestor, big_diff)
            big_diff = max(big_diff, right_big_diff)
        return big_diff
        
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        big_diff = self.find_big_diff_for_node(root, root.val, big_diff=0)
        if root.left:
            left_big_diff = self.maxAncestorDiff(root.left)
            big_diff = max(big_diff, left_big_diff)
        if root.right:
            right_big_diff = self.maxAncestorDiff(root.right)
            big_diff = max(big_diff, right_big_diff)
        return big_diff
