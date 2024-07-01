from all_possible_full_binary_trees import *

import pytest

@pytest.fixture()
def sol():
	return Solution()

# test allPossibleFBT

# Assert trees are equal
def assert_trees_are_equal(t1, t2):
	if t1 is None or t2 is None:
		assert t1 is None and t2 is None, f"Only one is None @ t1:{t1} t2:{t2}"
	
	assert t1.val == t2.val, f"Values don't match @ t1:{t1.val} t2:{t2.val}"

	if t1.left or t2.left:
		assert t1.left and t2.left, f"Missing left @ t1:{t1.val} t2:{t2.val}"
		assert_trees_are_equal(t1.left, t2.left)
	if t1.right or t2.right:
		assert t1.right and t2.right, f"Missing right @ t1:{t1.val} t2:{t2.val}"
		assert_trees_are_equal(t1.right, t2.right)

# expected tree for make_binary_tree_from_list
@pytest.fixture()
def expected_tree_from_list():
	'''
      0
     / \
	0   0
	   /
	  0
	'''
	root = TreeNode(0)
	root.left = TreeNode(0)
	root.right = TreeNode(0)
	root.right.left = TreeNode(0)
	return root

# test make_binary_tree_from_list
def test_make_binary_tree_from_list(sol, expected_tree_from_list):
	got = sol.make_binary_tree_from_list([0,0,0,None,None,0])

	assert_trees_are_equal(got, expected_tree_from_list)