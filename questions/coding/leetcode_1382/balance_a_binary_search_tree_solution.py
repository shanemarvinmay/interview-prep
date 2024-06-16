class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BST:
    def __init__(self, val) -> None:
        self.root = TreeNode(val)
    def add(self, val):
        itr = self.root
        while True:
            if itr.left and val <= itr.val:
                itr = itr.left
            elif itr.right and val > itr.val:
                itr = itr.right
            elif val <= itr.val:
                itr.left = TreeNode(val)
                return
            else:
                itr.right = TreeNode(val)
                return
		

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Get inorder array
        inorder = self.get_inorder_array(root, [])
        # Add to tree.
        root_idx = len(inorder) // 2
        tree = BST(inorder[root_idx])
        self.add_all_to_tree(tree, inorder, left=0, right=root_idx-1)
        self.add_all_to_tree(tree, inorder, left=root_idx+1, right=len(inorder)-1)
        
        return tree.root
        
    def get_inorder_array(self, root, ar):
        if root is None:
            return
        if root.left:
            self.get_inorder_array(root.left, ar)
        ar.append(root.val)
        if root.right:
            self.get_inorder_array(root.right, ar)
        return ar
    def add_all_to_tree(self, tree, inorder, left, right):
        if left > right:
            return
        mid = (left + right) // 2
        tree.add(inorder[mid])
        self.add_all_to_tree(tree, inorder, left, right=mid-1)
        self.add_all_to_tree(tree, inorder, left=mid+1, right=right)