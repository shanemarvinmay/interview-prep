from questions.coding.leetcode_2336.smallest_number_in_infinite_set import SmallestInfiniteSet

import pytest

def test_SmallestInfiniteSet():
    s = SmallestInfiniteSet()

    s.addBack(2)

    assert s.popSmallest() == 1
    assert s.popSmallest() == 2
    assert s.popSmallest() == 3

    s.addBack(1)

    assert s.popSmallest() == 1
    assert s.popSmallest() == 4
    assert s.popSmallest() == 5


'''
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[],                     [2],        [],            [],              [],          [1],       [],             [],            []]
[null,                  null,        1,            2,                3,           null,      1,               4,             5]
'''