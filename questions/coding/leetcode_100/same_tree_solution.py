# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p , q) -> bool:
        # if p q exist and have same value
        if p is None and q is None:
            return True
        elif (p and q is None) or (p is None and q):
            return False
        if p.val != q.val:
            return False
        # if p q have some children
        # return recursive call on children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)