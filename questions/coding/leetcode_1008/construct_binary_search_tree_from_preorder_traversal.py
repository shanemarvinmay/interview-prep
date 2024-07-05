from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        preorder.sort()
        return self.create_bst(preorder)
    def create_bst(self, nodes):
        if len(nodes) == 0:
            return
        root_idx = len(nodes) // 2
        root = TreeNode(nodes[root_idx])
        root.left = self.create_bst(nodes[:root_idx])
        root.right = self.create_bst(nodes[root_idx+1:])
        return root
        