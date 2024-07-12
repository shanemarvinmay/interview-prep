from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, l_root: TreeNode, r_root: TreeNode) -> List[int]:
        output = []
        l_stack = [l_root] if l_root else []
        r_stack = [r_root] if r_root else []

        while l_stack and r_stack:
            l_itr = l_stack.pop()
            r_itr = r_stack.pop()
            # Left
            while l_itr.left:
                l_stack.append(l_itr)
                l_itr = l_itr.left
                l_stack[-1].left = None
            while r_itr.left:
                r_stack.append(r_itr)
                r_itr = r_itr.left
                r_stack[-1].left = None
            # Parent
            if l_itr.val < r_itr.val:
                output.append(l_itr.val)
                # Handling right child since the parent was picked up.
                if l_itr.right:
                    l_stack.append(l_itr.right)
                r_stack.append(r_itr)
            else:
                output.append(r_itr.val)
                if r_itr.right:
                    r_stack.append(r_itr.right)
                l_stack.append(l_itr)
        # Leftovers
        while l_stack:
            l_itr = l_stack.pop()
            while l_itr.left:
                l_stack.append(l_itr)
                l_itr = l_itr.left
                l_stack[-1].left = None
            output.append(l_itr.val)
            if l_itr.right:
                l_stack.append(l_itr.right)
        while r_stack:
            r_itr = r_stack.pop()
            while r_itr.left:
                r_stack.append(r_itr)
                r_itr = r_itr.left
                r_stack[-1].left = None
            output.append(r_itr.val)
            if r_itr.right:
                r_stack.append(r_itr.right)
        return output
