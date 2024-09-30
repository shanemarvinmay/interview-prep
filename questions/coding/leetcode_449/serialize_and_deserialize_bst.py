from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ser = []
        self.tree_to_list(root, ser)
        while len(ser) and ser[-1] is None: ser.pop()
        return ','.join([str(num) for num in ser])
    def tree_to_list(self, root: Optional[TreeNode], ar: List[int], i:int = 0) -> Optional[TreeNode]:
        if root is None:
            return
        if len(ar) == 0:
            ar.append(root.val)
        left = i * 2 + 1
        right = i * 2 + 2
        while len(ar) < right + 1:
            ar.append(None)
        ar[left] = self.tree_to_list(root.left, ar, i=left)
        ar[right] = self.tree_to_list(root.right, ar, i=right)
        return root.val
    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        tree_list = data.split(',')
        root = self.list_to_tree(tree_list)
        return root
    def list_to_tree(self, tree_list: List, i=0):
        if i >= len(tree_list): return
        if tree_list[i] in ['None', ''] : return
        root = TreeNode(int(tree_list[i]))
        root.left = self.list_to_tree(tree_list, i*2+1)
        root.right = self.list_to_tree(tree_list, i*2+2)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans