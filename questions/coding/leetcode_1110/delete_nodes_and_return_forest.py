from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], targets: List[int]) -> List[TreeNode]:
        forest = []
        targets = set(targets)

        def helper(node, is_root):
            if node is None: return
            deleted = node.val in targets
            if is_root and not deleted: forest.append(node)
            node.left = helper(node.left, deleted)
            node.right = helper(node.right, deleted)
            return None if deleted else node
        helper(root, True)

        return forest
