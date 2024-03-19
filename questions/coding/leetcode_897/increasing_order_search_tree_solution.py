# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.head, self.tail = None, None
    # Attempt 0
    # def helper(self, root, nodes):
    #     if root is None:
    #         return
    #     self.helper(root.left, nodes)
    #     nodes.append(root)
    #     self.helper(root.right, nodes)
    def helper(self, root):
        if root is None:
            return 
        
        self.helper(root.left)
        # Now that we've gone left, we no longer need the left connection.
        root.left = None
        # If this is the bottom left node, it will become the head.
        if self.head is None:
            self.head = root
        else:
            # If this isn't the head, then we attach it to the tail and make it the new tail.
            self.tail.right = root
        self.tail = root

        self.helper(root.right)

    def increasingBST(self, root):
        self.helper(root)
        return self.head
        # Attempt 0
        # nodes = []
        # self.helper(root, nodes)
        # for i in range(1, len(nodes)):
        #     nodes[i-1].right = nodes[i]
        #     nodes[i-1].left = None
        #     nodes[i].left = None
        
        # return nodes[0]