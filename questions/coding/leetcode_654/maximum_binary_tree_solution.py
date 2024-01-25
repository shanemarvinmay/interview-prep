# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, left, right, nums):
        # If there is nothing left, right, or between left and right.
        if right < left or left >= len(nums):
            return
        
        max_idx = left
        for i in range(left, right+1):
            if nums[i] > nums[max_idx]:
                max_idx = i
        
        root = TreeNode(nums[max_idx])
        root.left = self.helper(left=left, right=max_idx-1, nums=nums)
        root.right = self.helper(left=max_idx+1, right=right, nums=nums)
        
        return root
    
    def constructMaximumBinaryTree(self, nums):
        if len(nums) < 1:
            return
        return self.helper(left=0, right=len(nums)-1, nums=nums)
        