from balance_a_binary_search_tree_solution import Solution, TreeNode

import pytest

def assert_trees_are_equal(r1, r2):
	if r1 is None or r2 is None:
		assert r1 is None and r2 is None
	
	assert r1.val == r2.val

	if r1.left or r2.left:
		assert r1.left and r2.left
		assert_trees_are_equal(r1.left, r2.left)
	if r1.right or r2.right:
		assert r1.right and r2.right
		assert_trees_are_equal(r1.right, r2.right)

'''
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
'''
@pytest.fixture()
def balanced_tree():
	balanced = TreeNode(2)
	balanced.left = TreeNode(1)
	balanced.right = TreeNode(3)
	return balanced

@pytest.fixture()
def unbalanced_tree():
	unbalanced = TreeNode(1)
	unbalanced.right = TreeNode(2)
	unbalanced.right.right = TreeNode(3)
	unbalanced.right.right.right = TreeNode(4)
	return unbalanced

@pytest.fixture()
def rebalanced_tree():
	rebalanced = TreeNode(3)
	rebalanced.left = TreeNode(1)
	rebalanced.right = TreeNode(4)
	rebalanced.left.right = TreeNode(2)
	return rebalanced

@pytest.mark.parametrize('root, expected', [
	("balanced_tree", "balanced_tree"),
	("unbalanced_tree", "rebalanced_tree")
])
def test_balance_BST(root, expected, request):
	root = request.getfixturevalue(root)
	expected = request.getfixturevalue(expected)
	solution = Solution()

	got = solution.balanceBST(root)

	assert_trees_are_equal(got, expected)
