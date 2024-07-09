from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        itr = head
        while itr:
            values.append(itr.val)
            itr = itr.next
        biggest = None
        length = len(values)
        for i in range(length//2):
            twin_sum = values[i] + values[length - i - 1]
            if biggest:
                biggest = max(biggest, twin_sum)
            else:
                biggest = twin_sum
        return biggest