from questions.coding.leetcode_2415.reverse_odd_levels_of_binary_tree import Solution, TreeNode
from questions.coding.util.util import assert_binary_trees_are_equal
import pytest
'''
Example 1:
Input: root = [2,3,5,8,13,21,34]
Output: [2,5,3,8,13,21,34]
Explanation: 
The tree has only one odd level.
The nodes at level 1 are 3, 5 respectively, which are reversed and become 5, 3.
Example 2:
Input: root = [7,13,11]
Output: [7,11,13]
Explanation: 
The nodes at level 1 are 13, 11, which are reversed and become 11, 13.
Example 3:
Input: root = [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
Output: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
Explanation: 
The odd levels have non-zero values.
The nodes at level 1 were 1, 2, and are 2, 1 after the reversal.
The nodes at level 3 were 1, 1, 1, 1, 2, 2, 2, 2, and are 2, 2, 2, 2, 1, 1, 1, 1 after the reversal.
Constraints:
The number of nodes in the tree is in the range [1, 214].
0 <= Node.val <= 105
root is a perfect binary tree.
'''
@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def two_level_tree():
    '''The tree and expected output will be returned as a tuple.
    The tree will look like this:
      1
     / \
    2   3'''
    input_root = TreeNode(1)
    input_root.left = TreeNode(2)
    input_root.right = TreeNode(3)

    expected_root = TreeNode(1)
    expected_root.left = TreeNode(3)
    expected_root.right = TreeNode(2)
    return input_root, expected_root

@pytest.mark.parametrize('test_case_fixture', [
    ('two_level_tree'),
])
def test_reverseOddLevels(test_case_fixture, request, sol):
    root, expected = request.getfixturevalue(test_case_fixture)

    got = sol.reverseOddLevels(root)

    assert_binary_trees_are_equal(got, expected)
