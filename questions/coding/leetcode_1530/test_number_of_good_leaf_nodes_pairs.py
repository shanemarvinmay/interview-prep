from questions.coding.leetcode_1530.number_of_good_leaf_nodes_pairs import Solution
from questions.coding.util.util import list_to_binary_tree

import pytest

@pytest.mark.parametrize('root, distance, expected', [
    ([1,2,3,None,4], 3,  1),
    ([1,2,3,4,5,6,7], 3, 2),
    ([7,1,4,6,None,5,3,None,None,None,None,None,2], 3, 1),
])
def test_countPairs(root, distance, expected):
    sol = Solution()
    root = list_to_binary_tree(root)

    got = sol.countPairs(root, distance)

    assert got == expected
