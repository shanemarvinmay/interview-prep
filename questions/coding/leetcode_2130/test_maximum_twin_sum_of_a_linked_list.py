from questions.coding.leetcode_2130.maximum_twin_sum_of_a_linked_list import Solution, ListNode

import pytest

@pytest.fixture()
def sol():
    return Solution()

@pytest.fixture()
def list_with_biggest_in_middle():
    head = ListNode(val=2)
    head.next = ListNode(val=4)
    head.next.next = ListNode(val=3)
    head.next.next.next = ListNode(val=1)
    return head
'''
Example 3:
Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.
'''

def test_pairSum(sol, list_with_biggest_in_middle):
    got = sol.pairSum(list_with_biggest_in_middle)

    assert got == 7