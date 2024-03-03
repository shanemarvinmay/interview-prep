# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        _, max_dist = self.helper(root)
        return max_dist
    
    def helper(self, root):
        if root is None:
            # dist, max_dist
            return 0, 0
        
        left_dist, left_max_dist = self.helper(root.left)
        right_dist, right_max_dist = self.helper(root.right)

        dist = left_dist + right_dist

        max_dist = max([dist, left_max_dist, right_max_dist])

        return max(left_dist, right_dist) + 1, max_dist