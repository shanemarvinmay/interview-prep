from collections import deque
from sum_of_nodes_with_even_valued_grandparent_solution import Solution

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_tree(input_list):
    if len(input_list) < 1:
        return
    
    root = TreeNode(input_list[0])
    q = deque([root])
    idx = 0

    while len(q):
        itr = q.popleft()
        if itr is None:
            idx += 1
            continue
        if 2 * idx + 1 < len(input_list) and input_list[2 * idx + 1]:
            node = TreeNode(input_list[2 * idx + 1])
            q.append(node)
            itr.left = node
        if 2 * idx + 2 < len(input_list) and input_list[2 * idx + 2]:
            node = TreeNode(input_list[2 * idx + 2])
            q.append(node)
            itr.right = node
        idx += 1
    
    return root

@pytest.mark.parametrize('input_list, expected, message', [
    ([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], 18, 'Evens, odds, lefts, and rights.'),
    ([1, 3, 5, 7, 9, 11], 0, 'Odds only.'),
    ([2, 4, 6, 8, 10, 12], 30, 'Evens only'),
    ([], 0, 'Empty tree')
])
def test_sum_even_grandparent(input_list, expected, message):
    solution = Solution()
    binary_tree = list_to_binary_tree(input_list)

    assert solution.sumEvenGrandparent(binary_tree) == expected, message