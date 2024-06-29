from solution import Solution, TreeNode

import pytest

@pytest.fixture()
def sol():
	solution = Solution()
	return solution

@pytest.fixture()
def one_sided_tree():
	"""
	1
	 \
	  2
	   \
	    0
	   /
	  3
	"""
	root = TreeNode(1)
	root.right = TreeNode(2)
	root.right.right = TreeNode(0)
	root.right.right.left = TreeNode(3)
	return root

@pytest.fixture()
def balanced_tree():
	root = TreeNode(8)
	root.left = TreeNode(3)
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(6)
	root.left.right.left = TreeNode(4)
	root.left.right.right = TreeNode(7)
	root.right = TreeNode(10)
	root.right.right = TreeNode(14)
	root.right.right.left = TreeNode(13)
	return root

@pytest.mark.parametrize('tree_fixture, expected', [
	('one_sided_tree', 3),
	('balanced_tree', 7),
])
def test_max_ancestor_diff(tree_fixture, expected, sol, request):
	tree = request.getfixturevalue(tree_fixture)

	assert sol.maxAncestorDiff(tree) == expected
