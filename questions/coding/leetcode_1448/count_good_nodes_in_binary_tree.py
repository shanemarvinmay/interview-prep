# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, cur_max=None, good_nodes=0) -> int:
        good_nodes = 0
        if root is None:
            return good_nodes
        if cur_max is None:
            cur_max = root.val
        cur_max = max(cur_max, root.val)
        
        good_nodes += self.goodNodes(root.left, cur_max, good_nodes)
        good_nodes += self.goodNodes(root.right, cur_max, good_nodes)

        if root.val >= cur_max:
            good_nodes += 1
        return good_nodes
