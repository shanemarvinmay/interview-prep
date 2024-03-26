"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # TODO implement it iteratively now.
    def _helper(self, root, nodes):
        if root is None:
            return
        if root.children:
            for child in root.children:
                self._helper(child, nodes)

        nodes.append(root.val)

    def postorder(self, root):
        nodes = []
        self._helper(root, nodes)
        return nodes


        