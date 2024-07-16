from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        num_to_node = dict()
        # These will be used to determine the root.
        parents, children = set(), set()

        for description in descriptions:
            parent, child, is_left = description
            parents.add(parent)
            children.add(child)
            # Making sure parent and child have nodes.
            if parent not in num_to_node:
                num_to_node[parent] = TreeNode(parent)
            if child not in num_to_node:
                num_to_node[child] = TreeNode(child)
            # Setting child relationship
            if is_left:
                num_to_node[parent].left = num_to_node[child]
            else:
                num_to_node[parent].right = num_to_node[child]
        
        # Finding the root.
        root = list(parents.difference(children))[0]
        return num_to_node[root]
