from middle_of_the_linked_list_solution import Solution

import pytest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

even_list = ListNode(1)
even_list.next = ListNode(2)
even_list.next.next = ListNode(3)
even_list.next.next.next = ListNode(4)

odd_list = ListNode(1)
odd_list.next = ListNode(2)
odd_list.next.next = ListNode(3)

@pytest.mark.parametrize("linked_list, expected", [
    (even_list, 3),
    (odd_list, 2)
])
def test_middle_node(linked_list, expected):
    solution = Solution()

    middle_node = solution.middleNode(linked_list)
    got = middle_node.val

    assert got == expected