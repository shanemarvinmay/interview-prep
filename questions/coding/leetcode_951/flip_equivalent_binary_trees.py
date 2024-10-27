from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if not self.nodes_same(n1, n2):
            return False
        if n1 is None or n2 is None:
            return True
        if self.nodes_same(n1.left, n2.left):
            return True and self.flipEquiv(n1.left, n2.left) and self.flipEquiv(n1.right, n2.right)
        elif self.nodes_same(n1.left, n2.right):
            return True and self.flipEquiv(n1.left, n2.right) and self.flipEquiv(n1.right, n2.left)
        else:
            return False
    def nodes_same(self, n1, n2):
        if n1 is None or n2 is None:
            return n1 is None and n2 is None
        return n1.val == n2.val
'''
951. Flip Equivalent Binary Trees
https://leetcode.com/problems/flip-equivalent-binary-trees/?envType=daily-question&envId=2024-10-24
'''
