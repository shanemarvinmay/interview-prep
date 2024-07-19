from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        nodes = self.get_nodes(root)
        i = 0

        while i < len(nodes):
            has_children = nodes[i].left is not None or nodes[i].right is not None
            if nodes[i].val == target and has_children == False:
                self.delete_child(root, target_node=nodes[i])
                del nodes[i]
            else:
                i += 1

        if nodes:
            return root
        return None

    def get_nodes(self, root, nodes=None):
        if nodes is None:
            nodes = []
        if root is None:
            return
        self.get_nodes(root.left, nodes)
        self.get_nodes(root.right, nodes)
        nodes.append(root)
        return nodes
    
    def delete_child(self, root, target_node):
        if root is None:
            return
        if root == target_node:
            del root
            return
        if root.left == target_node:
            root.left = None
            return
        if root.right == target_node:
            root.right = None
            return
        self.delete_child(root.left, target_node)
        self.delete_child(root.right, target_node)