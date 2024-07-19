from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.setup_tree(self.root)
    def setup_tree(self, root, cur=0):
        if root is None:
            return
        root.val = cur
        self.setup_tree(root.left, cur*2+1)
        self.setup_tree(root.right, cur*2+2)

    def find(self, target: int) -> bool:
        moves = []
        cur = target
        while cur:
            parent = self.get_parent(cur)
            if self.get_left_child(parent) == cur:
                moves.append('l')
            else:
                moves.append('r')
            cur = parent

        itr = self.root
        while moves:
            move = moves.pop()
            if itr is None:
                return False
            if move == 'l':
                itr = itr.left
            else:
                itr = itr.right
        return itr is not None and itr.val == target
    
    def get_parent(self, child):
        return (child - 1) // 2
    def get_left_child(self, parent):
        return parent * 2 + 1
    def get_right_child(self, parent):
        return self.get_left_child(parent) + 1

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)