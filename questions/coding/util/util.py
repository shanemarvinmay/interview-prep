from collections import deque

def assert_binary_trees_are_equal(t1, t2):
    if t1 is None or t2 is None:
        assert t1 is None and t2 is None
        return
    
    assert t1.val == t2.val

    assert_binary_trees_are_equal(t1.left, t2.left)
    assert_binary_trees_are_equal(t1.right, t2.right)

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