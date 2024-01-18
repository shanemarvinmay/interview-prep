# Definition for a binary tree node.
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def list_to_binary_tree(input_list):
    if not input_list:
        return
    
    mid = len(input_list) // 2
    root = TreeNode(input_list[mid])
    root.left = list_to_binary_tree(input_list[:mid])
    root.right = list_to_binary_tree(input_list[mid + 1:])

    return root

def binary_tree_to_list(root, input_list=[]):
    if root.left:
        binary_tree_to_list(root.left)

    input_list.append(root.value)

    if root.right:
        binary_tree_to_list(root.right)

    return input_list

class Solution:
    def helper(self, root: TreeNode, total=0) -> TreeNode:
        if root.right:
            total = self.helper(root.right, total)
        root.value += total
        if root.left:
            return self.helper(root.left, root.value)
        return root.value
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.helper(root)
        return root