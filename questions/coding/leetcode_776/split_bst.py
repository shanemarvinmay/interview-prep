from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.grtr = None
        self.less = None
    def add_node_less(self, node: TreeNode):
        if self.less is None:
            self.less = node
            return
        itr = self.less
        while itr:
            if itr == node:
                return
            if itr.val >= node.val:
                if itr.left:
                    itr = itr.left
                    continue
                itr.left = node
                return
            else:
                if itr.right:
                    itr = itr.right
                    continue
                itr.right = node
                return

    def add_node_grtr(self, node: TreeNode):
        if self.grtr is None:
            self.grtr = node
            return
        itr = self.grtr
        while itr:
            if itr == node:
                return
            if itr.val >= node.val:
                if itr.left:
                    itr = itr.left
                    continue
                itr.left = node
                return
            else:
                if itr.right:
                    itr = itr.right
                    continue
                itr.right = node
                return
    def helper(self, root: Optional[TreeNode], target: int):
        if root is None: return
        if root.val <= target:
            nxt = root.right
            if root.right and root.right.val > target:
                root.right = None
            self.add_node_less(root)
        else:
            nxt = root.left
            if root.left and root.left.val <= target:
                root.left = None
            self.add_node_grtr(root)
        self.helper(nxt, target)
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        self.grtr = None
        self.less = None
        self.helper(root, target)
        return [self.less, self.grtr]
