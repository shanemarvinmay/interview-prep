from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Attempt #1
class Solution:
    def __init__(self):
        self.root = None
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            self.add_node(preorder[i])
        return self.root
    def add_node(self, val):
        itr = self.root
        while True:
            if itr.left and val < itr.val:
                itr = itr.left
            elif itr.right and val > itr.val:
                itr = itr.right
            elif itr.val > val:
                itr.left = TreeNode(val)
                break
            else:
                itr.right = TreeNode(val)
                break

# Attempt #0
# class Solution:
#     def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
#         preorder.sort()
#         return self.create_bst(preorder)
#     def create_bst(self, nodes):
#         if len(nodes) == 0:
#             return
#         root_idx = len(nodes) // 2
#         root = TreeNode(nodes[root_idx])
#         root.left = self.create_bst(nodes[:root_idx])
#         root.right = self.create_bst(nodes[root_idx+1:])
#         return root
        