from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        self.j = 0
        
        return self.helper(preorder, postorder)
    def helper(self, preorder, postorder):
        root = TreeNode(preorder[self.i])
        self.i += 1
        if root.val != postorder[self.j]:
            root.left = self.helper(preorder, postorder)
        if root.val != postorder[self.j]:
            root.right = self.helper(preorder, postorder)
        self.j += 1
        return root
