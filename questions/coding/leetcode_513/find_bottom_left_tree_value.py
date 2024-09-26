from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        _, value = self.helper(root)
        return value
    def helper(self, root: TreeNode):
        if root.left is None and root.right is None:
            # distance, val
            return [1, root.val]
        left, right = [0,0], [0,0]
        if root.left:
            left = self.helper(root.left)
        if root.right:
            right = self.helper(root.right)
        # Deciding which node we should return based on which is further from
        # the root. If there is a tie, then we pick left.
        output = left
        if left[0] < right[0]:
            output = right
        # Inc distance
        output[0] += 1
        return output
