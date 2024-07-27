from questions.coding.leetcode_979.distribute_coins_in_binary_tree import Solution, TreeNode

import pytest
@pytest.fixture()
def sol():
    return Solution()        
'''
Input: root = [3,0,0]
Output: 2
Input: root = [0,3,0]
Output: 3
The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
'''
def test_distributeCoins(sol):
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(0)

    got = sol.distributeCoins(root)

    assert got == 2