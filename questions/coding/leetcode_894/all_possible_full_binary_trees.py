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
		self.n_to_forest = {1:[[0]], 3:[[0,0,0]]}
		
	def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
		if n % 2 == 0:
			return []
		if n in self.n_to_forest:
			return self.n_to_forest[n]
		
		for i in range(5, n+1, 2):
			self.n_to_forest[i] = []
			for tree in self.n_to_forest[i-2]:
				self.make_forest(tree, cur=0, num_trees=i)	
		
		return self.n_to_forest[n]

	def make_forest(self, tree, cur, num_trees):
		left = cur * 2 + 1
		right = cur * 2 + 2
		if right < len(tree) and tree[left] is not None and tree[right] is not None:
			self.make_forest(tree, left, num_trees)
			self.make_forest(tree, right, num_trees)
			return
		
		tree_copy = deepcopy(tree)
		# Append childrend to cur node in tree
		while right >= len(tree_copy):
			tree_copy.append(None)
		tree_copy[left] = 0
		tree_copy[right] = 0
		if tree_copy not in self.n_to_forest[num_trees]:
			self.n_to_forest[num_trees].append(tree_copy)

	def make_binary_tree_from_list(self, tree_list, idx=0):
		if idx >= len(tree_list) or tree_list[idx] is None:
			return
		tree_list[idx] = TreeNode(0)

		tree_list[idx].left = self.make_binary_tree_from_list(tree_list, idx*2+1)
		tree_list[idx].right = self.make_binary_tree_from_list(tree_list, idx*2+2)
		
		return tree_list[idx]

