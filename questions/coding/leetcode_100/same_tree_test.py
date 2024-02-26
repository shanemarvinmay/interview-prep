from same_tree_solution import Solution

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_tree(input_list):
    if not input_list:
        return
    
    mid = len(input_list) // 2
    root = TreeNode(input_list[mid])
    root.left = list_to_binary_tree(input_list[:mid])
    root.right = list_to_binary_tree(input_list[mid + 1:])

    return root


def binary_tree_to_list(root, input_list=[]):
    if root.left:
        binary_tree_to_list(root.left)

    input_list.append(root.value)

    if root.right:
        binary_tree_to_list(root.right)

    return input_list

@pytest.mark.parametrize('p, q, expected, message', [
    ([0,1,2], [0,1,2], True, 'Same trees with children - True'),
    ([0,1,None,2], [0,1,2], False, 'Diff shape - False'),
    ([0, 1, 2], [3, 4, 5], False, 'Diff values - False')
])
def test_is_same_tree(p, q, expected, message):
    solution = Solution()
    p = list_to_binary_tree(p)
    q = list_to_binary_tree(q)

    got = solution.isSameTree(p, q)

    assert got == expected