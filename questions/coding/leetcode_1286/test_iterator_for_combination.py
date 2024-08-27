from questions.coding.leetcode_1286.iterator_for_combination import CombinationIterator
from collections import deque

def test_get_combos():
    combo_itr = CombinationIterator('abc', 2)

    assert list(combo_itr.combos) == ['ab', 'ac', 'bc']

def test_CombinationIterator():
    expected = deque(['ab', 'ac', 'bc'])
    combo_itr = CombinationIterator('abc', 2)

    while combo_itr.hasNext():
        assert combo_itr.next() == expected.popleft()
    
    assert len(combo_itr.combos) == 0
