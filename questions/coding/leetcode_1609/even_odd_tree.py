from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        hash_map = dict()

        def dfs(node: TreeNode, level: int):
            if node is None: return True
            # Checking node value
            if node.val % 2 == level % 2: return False
            # Check inc/dec order
            if level not in hash_map:
                hash_map[level] = [node.val]
            elif level % 2 == 0 and node.val <= hash_map[level][-1]:
                return False
            elif level % 2 == 1 and node.val >= hash_map[level][-1]:
                return False
            else:
                hash_map[level].append(node.val)
            
            return dfs(node.left, level+1) and dfs(node.right, level+1)
        
        return dfs(root, 0)
