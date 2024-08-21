from questions.coding.leetcode_2487.remove_nodes_from_linked_list import ListNode, Solution

# some are deleted (begining and middle)
# In: 1 -> 10 -> 2 -> 3 -> 8
# Out: 10 -> 8

def test_removeNodes():
    # 10 -> 8
    expected = ListNode(10, ListNode(8))
    # 1 -> 10 -> 2 -> 3 -> 8
    head = ListNode(1, ListNode(10, ListNode(2, ListNode(3, ListNode(8)))))
    sol = Solution()

    got = sol.removeNodes(head)

    while got and expected:
        assert got.val == expected.val
        got = got.next
        expected = expected.next
    assert got == expected 
