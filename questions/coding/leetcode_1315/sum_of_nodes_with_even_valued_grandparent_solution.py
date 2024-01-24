# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, grandparent_even=False, parent_even=False):
        if root is None:
            return 0
        
        total = root.val if grandparent_even else 0
        grandparent_even = parent_even
        parent_even = root.val % 2 == 0
        return total + self.helper(root.left, grandparent_even, parent_even) + self.helper(root.right, grandparent_even, parent_even)
    
    def sumEvenGrandparent(self, root):
        return self.helper(root)