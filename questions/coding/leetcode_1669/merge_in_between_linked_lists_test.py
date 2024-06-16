from merge_in_between_linked_lists_solution import Solution, ListNode

def test_merge_in_between():
	list1 = ListNode(0)
	list1.next = ListNode(1)
	list1.next.next = ListNode(2)

	list2 = ListNode('a')

	expected = ListNode(0)
	expected.next = ListNode('a')
	expected.next.next = ListNode(2)

	solution = Solution()

	got = solution.mergeInBetween(list1=list1, a=1, b=1, list2=list2)

	while got and expected:
		assert got.val == expected.val
		got = got.next
		expected = expected.next
	assert got is None and expected is None
