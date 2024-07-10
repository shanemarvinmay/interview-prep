from questions.coding.leetcode_237.delete_node_in_a_linked_list import Solution, ListNode

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def test_case():
    head = ListNode(0)
    head.next = ListNode(-1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    return {
        "head":head,
        "target":head.next
    }

def test_deleteNode(sol, test_case):
    target_val = test_case['target'].val

    sol.deleteNode(test_case['target'])

    itr = test_case['head']
    while itr:
        assert itr.val != target_val
        itr = itr.next
