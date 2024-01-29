# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        # root is None
        if root is None:
            return
        # root is match
        elif root.val == val:
            return root
        # root > value
        elif root.val > val:
            return self.searchBST(root.left, val)
        # root < value
        return self.searchBST(root.right, val)
