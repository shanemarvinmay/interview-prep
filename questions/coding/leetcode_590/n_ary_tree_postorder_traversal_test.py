from n_ary_tree_postorder_traversal_solution import Solution

import pytest

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

@pytest.fixture(scope='module')
def basic_tree():
    nodes = [Node(i) for i in range(7)]
    root = nodes[1]
    root.children = [nodes[3], nodes[2], nodes[4]]
    nodes[3].children = [nodes[5], nodes[6]]
    return root


def test_post_order(basic_tree):
    expected = [5,6,3,2,4,1]
    solution = Solution()

    got = solution.postorder(basic_tree)

    assert len(got) == len(expected)
    
    for i in range(len(expected)):
        assert got[i] == expected[i]