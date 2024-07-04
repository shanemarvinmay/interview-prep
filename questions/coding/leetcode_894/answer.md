# Intuition
The recursion works by first generating all possible full binary trees with i nodes, and then all possible full binary trees with n - i - 1 nodes. For each pair of trees, a new tree is created with the first tree as the left subtree and the second tree as the right subtree. This process is repeated until all possible trees with n nodes have been generated.

# Approach
Initialize a hash table to store the generated trees.
If n is even, return an empty list.
If n is 1, add a new tree to the hash table.
For i from 1 to n - 1, do:
Generate all possible full binary trees with i nodes.
Generate all possible full binary trees with n - i - 1 nodes.
For each pair of trees, create a new tree with the first tree as the left subtree and the second tree as the right subtree.
Add the new tree to the hash table.
Return the list of trees in the hash table.
Complexity
Time complexity: O(2^n)
Space complexity: O(n)
# Code
```
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}

        def _allPossibleFBT(n):
            if n in memo:
                return memo[n]

            list = []
            if n == 1:
                list.append(TreeNode(0))
            else:
                for i in range(1, n - 1, 2):
                    lTrees = _allPossibleFBT(i)
                    rTrees = _allPossibleFBT(n - i - 1)

                    for lt in lTrees:
                        for rt in rTrees:
                            list.append(TreeNode(0, lt, rt))

            memo[n] = list
            return list

        return _allPossibleFBT(n)
```