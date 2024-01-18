from binary_search_tree_to_greater_sum_tree_solution import *

import pytest

@pytest.fixture()
def bst_to_gst():
    s = Solution()
    return s.bstToGst

@pytest.fixture()
def input_list():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8]

@pytest.fixture()
def example_tree():
    '''This is the binary search tree version of the list from `input_list`.'''
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(0)
    root.right = TreeNode(7)
    root.right.left = TreeNode(6)
    root.right.left.left = TreeNode(5)
    root.right.right = TreeNode(8)
    return root

def assert_binary_trees_are_equal(root1, root2):
    '''This function asserts 2 binary trees have the same shape and values.'''
    # Either both roots must be None or both must exist
    assert (root1 is None and root2 is None) or (root1 and root2)
    if root1 is None and root2 is None:
        return
    # Roots have same value.
    # print(root1.value, root2.value)
    assert root1.value == root2.value
    # Roots both have lefts or both do not have lefts.
    assert (root1.left is None and root2.left is None) or (root1.left and root2.left)
    if root1.left and root2.left:
        # print('Left')
        assert_binary_trees_are_equal(root1.left, root2.left)
    # Roots have both have rights both do not have rights.
    assert (root1.right is None and root2.right is None) or (root1.right and root2.right)
    if root1.right and root2.right:
        # print('Right')
        assert_binary_trees_are_equal(root1.right, root2.right)

def test_list_to_binary_tree(input_list, example_tree):
    got_tree = list_to_binary_tree(input_list)

    assert_binary_trees_are_equal(got_tree, example_tree)

def test_binary_tree_to_list(input_list, example_tree):
    got_list = binary_tree_to_list(example_tree)

    assert got_list == input_list

def test_Solution_bstToGst_lefts_and_rights(bst_to_gst, example_tree):
    expected_tree = list_to_binary_tree([36, 36, 35, 33, 30, 26, 21, 15, 8])

    got_tree = bst_to_gst(example_tree)

    assert_binary_trees_are_equal(got_tree, expected_tree)


def print_binary_tree(root):
    '''I got this code from https://leetcode.com/discuss/interview-question/1954462/pretty-printing-binary-trees-in-python-for-debugging.
    Only small changes have been made.'''
    lines, *_ = _print_binary_tree_aux(root)
    for line in lines:
        print(line)

def _print_binary_tree_aux(self):
    """Returns list of strings, width, height, and horizontal coordinate of the root."""
    # No child.
    if self.right is None and self.left is None:
        line = '%s' % self.value
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    # Only left child.
    if self.right is None:
        lines, n, p, x = _print_binary_tree_aux(self.left)
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    # Only right child.
    if self.left is None:
        lines, n, p, x = _print_binary_tree_aux(self.right)
        s = '%s' % self.value
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    # Two children.
    left, n, p, x = _print_binary_tree_aux(self.left)
    right, m, q, y = _print_binary_tree_aux(self.right)
    s = '%s' % self.value
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2