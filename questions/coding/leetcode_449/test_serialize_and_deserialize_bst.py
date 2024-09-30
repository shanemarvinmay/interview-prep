from questions.coding.leetcode_449.serialize_and_deserialize_bst import Codec
from questions.coding.util.util import assert_binary_trees_are_equal, list_to_binary_tree

import pytest

@pytest.mark.parametrize('tree_list, expected', [
 ([2,1,3], '2,1,3'),
 ([],''),
 ([2,None,3], '2,None,3'),
 ([5,3,6,2,4,None,None,1], '5,3,6,2,4,None,None,1'),
])
def test_serialize(tree_list, expected):
    codec = Codec()
    tree = list_to_binary_tree(tree_list)

    got = codec.serialize(tree)

    assert got == expected

@pytest.mark.parametrize('tree_str, expected', [
 ('2,1,3', [2,1,3]),
 ('', []),
 ('2,None,3', [2,None,3]),
('5,3,6,2,4,None,None,1', [5,3,6,2,4,None,None,1]),
])
def test_deserialize(tree_str, expected):
    codec = Codec()
    expected = list_to_binary_tree(expected)

    got = codec.deserialize(tree_str)

    assert_binary_trees_are_equal(got, expected)
'''
449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/
Constraints:
The encoded string should be as compact as possible.
The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
'''
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans