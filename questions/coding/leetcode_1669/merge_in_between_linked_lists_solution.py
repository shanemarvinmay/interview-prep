# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
		# Finding the node right before a.
		a_itr = list1
		count = 0
		while count != a - 1:
			a_itr = a_itr.next
			count += 1
		# Finding the node right before b.
		b_itr = a_itr
		while count != b:
			b_itr = b_itr.next
			count += 1
		# Removing pointer from b to the rest of the linked list.
		temp = b_itr
		b_itr = b_itr.next
		temp.next = None
		# Having the node before a point to list2's head.
		a_itr.next = list2
		# Getting the tail of list 2 and pointing it to the node after b
		# (which is what b_itr currently is).
		list2_itr = list2
		while list2_itr.next:
			list2_itr = list2_itr.next
		list2_itr.next = b_itr

		return list1
        