from typing import List, Optional
from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
	def __init__(self):
		self.n_to_forest = dict()
		
	def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
		if n in self.n_to_forest:
			return self.n_to_forest[n]
		
		forest = []
		if n % 2:
			self.helper(n, forest)

		self.n_to_forest[n] = forest

		return forest
		
	def helper(self, n, forest, tree=None, cur=None):
		if tree is None:
			tree = [0]
		if cur is None:
			cur = 0

		if (cur == 0 and n < 3) or n < 2:
			return
		
		left = cur * 2 + 1
		right = cur * 2 + 2

		while right >= len(tree):
			tree.append(None)
		tree[left] = 0
		tree[right] = 0

		self.helper(n-2, forest, tree, left)
		if n - 2 > 0:
			tree_copy = deepcopy(tree)
			self.helper(n-2, forest, tree_copy, right)
		
		forest.append(tree)
            
	def make_binary_tree_from_list(self, tree_list, idx=0):
		if idx >= len(tree_list) or tree_list[idx] is None:
			return
		tree_list[idx] = TreeNode(0)

		tree_list[idx].left = self.make_binary_tree_from_list(tree_list, idx*2+1)
		tree_list[idx].right = self.make_binary_tree_from_list(tree_list, idx*2+2)
		
		return tree_list[idx]

