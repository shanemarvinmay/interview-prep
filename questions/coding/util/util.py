def assert_binary_trees_are_equal(t1, t2):
    if t1 is None or t2 is None:
        assert t1 is None and t2 is None
        return
    
    assert t1.val == t2.val

    assert_binary_trees_are_equal(t1.left, t2.left)
    assert_binary_trees_are_equal(t1.right, t2.right)
