from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        odd_level = True

        while stack:
            q = []
            while stack:
                itr = stack.pop()
                if itr.left and itr.right:
                    q.append(itr.left)
                    q.append(itr.right) 
            stack = q
            if odd_level:
                self.reverse_vals(stack)
            odd_level = not odd_level

        return root
    def reverse_vals(self, nodes):
        start = 0
        end = len(nodes) - 1
        while start < end:
            nodes[start].val, nodes[end].val =  nodes[end].val, nodes[start].val
            start += 1
            end -= 1  
                   

