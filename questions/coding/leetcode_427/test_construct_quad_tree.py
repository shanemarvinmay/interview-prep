from questions.coding.leetcode_427.construct_quad_tree import Node, Solution

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def grid():
    return [
        [1,1,0,0],
        [1,1,1,1],
        [0,0,1,1],
        [0,0,1,1],
    ]

@pytest.fixture()
def expected_tree():
    tl = Node(
        val=1,
        isLeaf=1,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None
    )
    tr_tl = Node(
        val=0,
        isLeaf=1,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None
    )
    tr_tr = Node(
        val=0,
        isLeaf=1,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None
    )
    tr_bl = Node(
        val=1,
        isLeaf=1,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None
    )
    tr_br = Node(
        val=1,
        isLeaf=1,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None
    )
    tr = Node(
        val=0,
        isLeaf=0,
        topLeft=tr_tl,
        topRight=tr_tr,
        bottomLeft=tr_bl,
        bottomRight=tr_br
    )
    bl = Node(
        val=0,
        isLeaf=1,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None
    )
    br = Node(
        val=1,
        isLeaf=1,
        topLeft=None,
        topRight=None,
        bottomLeft=None,
        bottomRight=None
    )
    return Node(
        val=0,
        isLeaf=0,
        topLeft=tl,
        topRight=tr,
        bottomLeft=bl,
        bottomRight=br
    )

def assert_trees_are_equal(t1: Node, t2: Node):
    if t1 is None or t2 is None:
        assert t1 is None and t2 is None
        return
    if t1.isLeaf or t2.isLeaf:
        assert t1.val == t2.val
        assert t1.isLeaf == t2.isLeaf
    assert_trees_are_equal(t1.topLeft, t2.topLeft)
    assert_trees_are_equal(t1.topRight, t2.topRight)
    assert_trees_are_equal(t1.bottomLeft, t2.bottomLeft)
    assert_trees_are_equal(t1.bottomRight, t2.bottomRight)

def test_construct(sol, grid, expected_tree):
    got_tree = sol.construct(grid)

    assert_trees_are_equal(got_tree, expected_tree)

@pytest.mark.parametrize('grid, expected', [
    ([[0,1],[2,3]], ([[0]],[[1]],[[2]],[[3]])),
    ([
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]
    ], ([[0,1],[4,5]],
        [[2,3],[6,7]],
        [[8,9],[12,13]],
        [[10,11],[14,15]])),
])
def test_get_corners(grid, expected, sol):
    got = sol.get_corners(grid)

    assert got == expected

@pytest.mark.parametrize('grid, expected', [
    ([0,0], True),
    ([[1,1],[0,1]], False),
])
def test_is_all_one_value(grid, expected, sol):
    got = sol.is_all_one_value(grid)

    assert got == expected

@pytest.mark.parametrize('grid, expected', [
    ([1], 1),
    ([[0,0],[0,0]], 0),
])
def test_get_val(grid, expected, sol):
    got = sol.get_val(grid)

    assert got == expected
