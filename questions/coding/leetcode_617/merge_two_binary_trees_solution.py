# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1, root2):
        if root1 and root2:
            root1.val += root2.val
        elif root1 is None and root2:
            root1 = root2
            return root1
        else:
            return root1
        
        if root1.left or root2.left and root1 != root2:
            if root1.left is None:
                root1.left = root2.left
            else:
                self.mergeTrees(root1.left, root2.left)
        
        if root1.right or root2.right and root1 != root2:
            if root1.right is None:
                root1.right = root2.right
            else:
                self.mergeTrees(root1.right, root2.right)
        
        return root1