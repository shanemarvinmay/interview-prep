Intuition:
Find the left part and right part,
then recursively construct the tree.

```
    def bstFromPreorder(self, A):
        return self.buildTree(A[::-1], float('inf'))

    def buildTree(self, A, bound):
        if not A or A[-1] > bound: return None
        node = TreeNode(A.pop())
        node.left = self.buildTree(A, node.val)
        node.right = self.buildTree(A, bound)
        return node
```