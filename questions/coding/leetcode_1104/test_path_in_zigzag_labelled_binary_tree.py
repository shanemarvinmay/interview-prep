from questions.coding.leetcode_1104.path_in_zigzag_labelled_binary_tree import Solution

import pytest


@pytest.fixture()
def sol():
    return Solution()

@pytest.mark.parametrize('label, expected', [
    (14, [1,3,4,14]),
    (26, [1,2,6,10,26]),
])
def test_pathInZigZagTree(label, expected, sol):
    got = sol.pathInZigZagTree(label)

    assert got == expected