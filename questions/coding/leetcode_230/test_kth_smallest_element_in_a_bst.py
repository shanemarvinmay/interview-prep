from questions.coding.leetcode_230.kth_smallest_element_in_a_bst import Solution, TreeNode

import pytest

@pytest.fixture()
def a_tree():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    return root

@pytest.fixture()
def another_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    return root

@pytest.mark.parametrize('root, k, expected', [
    ('a_tree', 1, 1),
    ('another_tree', 3, 3),
])
def test_kthSmallest(root, k, expected, request):
    sol = Solution()
    root = request.getfixturevalue(root)

    got = sol.kthSmallest(root, k)

    assert got == expected
