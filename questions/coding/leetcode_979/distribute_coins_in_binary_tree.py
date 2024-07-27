from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves, _ = self.helper(root)
        return moves
    def helper(self, root: Optional[TreeNode], moves=0, balance=0):
        if root is None:
            return moves, balance
        
        left_moves, left_balance = self.helper(root.left)
        right_moves, right_balance = self.helper(root.right)

        balance += left_balance + right_balance
        moves += left_moves + right_moves

        balance += root.val - 1
        moves += abs(balance)

        return moves, balance