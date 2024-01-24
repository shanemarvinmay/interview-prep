from sum_of_nodes_with_even_valued_grandparent_solution import Solution

'''
TODO:
1. List to tree. [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
2. Test when there is no evens. [1]
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def test_sum_even_grandparent():
    expected = 18
    solution = Solution()
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(8)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(5)

    assert solution.sumEvenGrandparent(root) == expected