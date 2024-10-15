from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        self.odd_head = self.odd = self.even_head = self.even = None
        i = 1
        itr = head
        
        while itr:
            if i % 2:
                self.append_to_odd(itr)
            else:
                self.append_to_even(itr)
            i += 1
            itr = itr.next
        
        self.odd.next = self.even_head
        if self.even:
            self.even.next = None
        return self.odd_head

    def append_to_odd(self, new_node: ListNode):
        if self.odd_head is None:
            self.odd_head = new_node
            self.odd = self.odd_head
            return
        self.odd.next = new_node
        self.odd = new_node
    def append_to_even(self, new_node: ListNode):
        if self.even_head is None:
            self.even_head = new_node
            self.even = self.even_head
            return
        self.even.next = new_node
        self.even = new_node
