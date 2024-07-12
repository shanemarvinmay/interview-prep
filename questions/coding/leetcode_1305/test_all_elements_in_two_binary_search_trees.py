from questions.coding.leetcode_1305.all_elements_in_two_binary_search_trees import Solution, TreeNode

import pytest
'''
Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

!!! Empty test case !!!
Constraints:
The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105'''

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def left_tree():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    return root

@pytest.fixture()
def right_tree():
    root = TreeNode(1)
    root.right = TreeNode(8)
    return root

@pytest.fixture()
def none():
    return None

@pytest.mark.parametrize('l_root, r_root, expected', [
    # ('left_tree', 'right_tree', [1,1,2,4,8]),
    ('left_tree', 'none', [1,2,4]),
])
def test_getAllElements(l_root, r_root, expected, request, sol):
    l_root = request.getfixturevalue(l_root)
    r_root = request.getfixturevalue(r_root)

    got = sol.getAllElements(l_root, r_root)

    assert got == expected
