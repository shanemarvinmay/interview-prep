from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        root.val = 0
        while stack:
            nxt_lvl = []
            total = 0
            while stack:
                itr = stack.pop()
                if not itr: continue
                siblings = []
                if itr.left:
                    siblings.append(itr.left)
                    total += itr.left.val
                if itr.right:
                    siblings.append(itr.right)
                    total += itr.right.val
                if siblings:
                    nxt_lvl.append(siblings)
            for siblings in nxt_lvl:
                if len(siblings) == 2:
                    sibling_total = siblings[0].val + siblings[1].val
                else:
                    sibling_total = siblings[0].val
                cousin_total = total - sibling_total
                for sibling in siblings:
                    sibling.val = cousin_total
                    stack.append(sibling)
        return root