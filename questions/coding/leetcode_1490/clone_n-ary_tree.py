from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: Node) -> 'Node':
        if root is None: return
        children = []
        for child in root.children:
            children.append(self.cloneTree(child))
        return Node(root.val, children)
'''
1490. Clone N-ary Tree
https://leetcode.com/problems/clone-n-ary-tree/
'''
'''
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
The total number of nodes is between [0, 104].
'''