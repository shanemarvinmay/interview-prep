from questions.coding.leetcode_96.unique_binary_search_trees import Solution

import pytest

sol = Solution()

def test_numTrees():
    n = 5
    expected = 42

    got = sol.numTrees(5)

    assert got == expected