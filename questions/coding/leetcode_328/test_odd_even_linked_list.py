from questions.coding.leetcode_328.odd_even_linked_list import ListNode, Solution

import pytest

@pytest.mark.parametrize('ll, expected, msg', [
    # (None, None, 'Empty list'),
    # (ListNode(1), ListNode(1), '1->None'),
    # (ListNode(1, next=ListNode(2)), 
    #  ListNode(1, next=ListNode(2)), 
    #  '1->2->None' ),
    (ListNode(1, next=ListNode(2, next=ListNode(3))), 
     ListNode(1, next=ListNode(3, next=ListNode(2))), 
     '1->2->3->None' ),
    (ListNode(1, next=ListNode(2, next=ListNode(3, next=ListNode(4)))), 
     ListNode(1, next=ListNode(3, next=ListNode(2, next=ListNode(4)))), 
     '1->2->3->4->None' ),
])
def test_oddEvenList(ll, expected, msg):
    sol = Solution()

    got = sol.oddEvenList(ll)

    while got and expected:
        assert got.val == expected.val
        got = got.next
        expected = expected.next
    
    assert got is None and expected is None
