from questions.coding.leetcode_2196.create_binary_tree_from_descriptions import Solution, TreeNode
from questions.coding.util.util import assert_binary_trees_are_equal
import pytest

@pytest.fixture()
def sol():
    return Solution()
'''
Another example not covered here
Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]

[[39,70,1],[13,39,1],[85,74,1],[74,13,1],[38,82,1],[82,85,1]]
[74,13,null,39,null,70]
'''
@pytest.fixture()
def normal_tree():
    root = TreeNode(50)

    root.left = TreeNode(20)
    root.left.left = TreeNode(15)
    root.left.right = TreeNode(17)

    root.right = TreeNode(80)
    root.right.left = TreeNode(19)

    return root

@pytest.fixture()
def left_only_tree():
    root = TreeNode(38)
    root.left = TreeNode(82)
    root.left.left = TreeNode(85)
    root.left.left.left = TreeNode(74)
    root.left.left.left.left = TreeNode(13)
    root.left.left.left.left.left = TreeNode(39)
    root.left.left.left.left.left.left = TreeNode(70)
    return root

@pytest.mark.parametrize('descriptions, expected', [
    ([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]], 'normal_tree'),
    ([[39,70,1],[13,39,1],[85,74,1],[74,13,1],[38,82,1],[82,85,1]], 'left_only_tree')
])
def test_createBinaryTree(descriptions, expected, request, sol):
    expected = request.getfixturevalue(expected)

    got = sol.createBinaryTree(descriptions)

    assert_binary_trees_are_equal(got, expected)
