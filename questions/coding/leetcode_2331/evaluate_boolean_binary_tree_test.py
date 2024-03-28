from evaluate_boolean_binary_tree_solution import Solution

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

@pytest.fixture(scope='module')
def full_tree_results_true():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    return root

@pytest.fixture(scope='module')
def just_root_results_false():
    root = TreeNode(0)
    return root

@pytest.mark.parametrize('root, expected', [
    ('full_tree_results_true', True),
    ('just_root_results_false', False)
])
def test_evaluate_tree(root, expected, request):
    solution = Solution()
    root = request.getfixturevalue(root)

    got = solution.evaluateTree(root)

    assert got == expected
