# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance_limit: int) -> int:
        self.distance_limit = distance_limit
        self.pairs = 0
        self.helper(root)
        return self.pairs
    def helper(self, root):
        # Child
        if root.left is None and root.right is None:
            return [1]
        left_children_dists = []
        right_children_dists = []
        if root.left:
            left_children_dists = self.helper(root.left)
        if root.right:
            right_children_dists = self.helper(root.right)
        # Counting pairs.
        for left_child_dist in left_children_dists:
            for right_child_dist in right_children_dists:
                if left_child_dist + right_child_dist <= self.distance_limit:
                    self.pairs += 1
        # Updating and sending up children distances.
        left_children_dists.extend(right_children_dists)
        for i in range(len(left_children_dists)):
            left_children_dists[i] += 1
        return left_children_dists
