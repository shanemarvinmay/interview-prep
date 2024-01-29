from search_in_a_binary_search_tree_solution import Solution

import pytest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_binary_search_tree(input_list):
    '''list_to_binary_search_tree turns a list representing a binary search tree into an actual binary search tree made of nodes.'''
    if len(input_list) < 1:
        return
    
    input_list[0] = TreeNode(input_list[0])
    for i in range(len(input_list)):
        left_idx = 2 * i + 1
        if left_idx < len(input_list):
            input_list[left_idx] = TreeNode(input_list[left_idx])
            input_list[i].left = input_list[left_idx]
        right_idx = 2 * i + 2
        if right_idx < len(input_list):
            input_list[right_idx] = TreeNode(input_list[right_idx])
            input_list[i].right = input_list[right_idx]

    return input_list[0]

def binary_search_tree_to_list(root):
    '''binary_search_tree_to_list creates a list representing the inputted binary search tree.'''
    if root is None:
        return
    
    bst_list = [root]
    i = 0
    while i < len(bst_list):
        itr = bst_list[i]
        if itr.left:
            bst_list.append(itr.left)
        if itr.right:
            bst_list.append(itr.right)
        i += 1

    return [i.val for i in bst_list]

@pytest.mark.parametrize('bst_list, target, expected, message', [
    ([], 0, None, 'Empty tree.'),
    ([4, 2, 7, 1, 3], 3, 3, 'Lefts and rights needed to find target.'),
    ([4, 2, 7, 1, 3], 6, None, 'No match, target is not in bst.')
])
def test_search_bst(bst_list, target, expected, message):
    solution = Solution()
    bst = list_to_binary_search_tree(bst_list)

    got = solution.searchBST(bst, target)
    got = got.val if got else None

    assert got == expected, message
