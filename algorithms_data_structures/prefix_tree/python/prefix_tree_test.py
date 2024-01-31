from prefix_tree import *

def assert_trees_are_equal(t1, t2):
    # Roots are None, or both are not.
    if t1 is None:
        assert t2 is None
        return
    else:
        assert t2 is not None
    # Values match.
    assert t1.value == t2.value
    # Number of children match.
    assert len(t1.children.keys()) == len(t2.children.keys())
    # call for children if they have any
    for child in t1.children:
        assert_trees_are_equal(t1.children[child], t2.children[child])

def test_convert_list_to_prefix_tree_nodes():
    # at ate
    t = TreeNode(value='t',children={'*': TreeNode('*'), 'e': TreeNode('e', children={'*': TreeNode('*')})})
    a = TreeNode(value='a', children={'t':t})
    # it
    i = TreeNode(value='i', children={'t': TreeNode('t', children={'*': TreeNode('*')})})
    expected = TreeNode(children={'a': a, 'i': i})
    words = ['at', 'ate', 'it']

    got = convert_list_to_prefix_tree_nodes(words)

    assert_trees_are_equal(got, expected)
