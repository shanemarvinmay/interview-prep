from questions.coding.leetcode_776.split_bst import Solution, TreeNode
from questions.coding.util.util import list_to_binary_tree

tree = [10,5,20,3,9,15,25,None,None,8,None,None,None,None,None,6,None,None,7]

'''
    5
     \
      9
     /
    7
   /\
  6  8
'''
one_sided = TreeNode(5, right=TreeNode(9, left=TreeNode(7, left=TreeNode(6), right=TreeNode(8))))

failed_test_case = list_to_binary_tree(tree)

def test_splitBST():
    sol = Solution()

    less, grtr = sol.splitBST(failed_test_case, 6)

    assert True

