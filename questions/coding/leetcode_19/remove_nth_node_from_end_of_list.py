from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None: return
        s = f = head
        s_count, f_count = 1, 0

        while f:
            f = f.next
            f_count += 1
            if f:
                f = f.next
                f_count += 1
            if f:
                s = s.next
                s_count += 1
        
        if n == f_count:
            return head.next
        
        target = f_count - n + 1

        if target < s_count:
            s_count = 1
            s = head
        
        while s_count + 1 < target:
            s = s.next
            s_count += 1
        
        s.next = s.next.next

        return head