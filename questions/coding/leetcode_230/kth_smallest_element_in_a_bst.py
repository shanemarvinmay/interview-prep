from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = []
        self.create_k_smallest(smallest, root, k)
        return smallest[k-1]

    def create_k_smallest(self, smallest: List, root: Optional[TreeNode], k: int):
        if root is None or len(smallest) == k:
            return
        self.create_k_smallest(smallest, root.left, k)
        smallest.append(root.val)
        self.create_k_smallest(smallest, root.right, k)
