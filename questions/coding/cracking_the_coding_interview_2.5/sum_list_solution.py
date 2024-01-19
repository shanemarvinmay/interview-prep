# Check out the textbook solution: https://github.com/careercup/CtCI-6th-Edition-Python/blob/e6bc732588601d0a98e5b1bc44d83644b910978d/Chapter2/5_Sum_Lists.py

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    

def sum_list(head1, head2):
    carry_over = 0
    i = head1
    j = head2
    tail = head1

    while i and j:
        total = i.val + j.val + carry_over
        carry_over = 1 if total > 9 else 0
        i.val = total % 10

        tail = i
        i = i .next
        j = j.next
    
    # If list 2 (from head2) is longer
    while j and tail:
        total = j.val + carry_over
        carry_over = 1 if total > 9 else 0
        tail.next = Node(total % 10)
        
        tail = tail.next
        j = j.next
    
    while carry_over:
        total = tail.val + carry_over
        carry_over = 1 if total > 9 else 0
        
        if tail.next is None and carry_over:
            tail.next = Node(carry_over)
            break
        tail.next = Node(total % 10)
        tail = tail.next
    
    return head1 if head1 else head2

def list_to_num(head):
    nums = []
    itr = head
    while itr:
        nums.append(itr.val)
        itr = itr.next
    nums.reverse()

    num = 0
    for i in nums:
        num = num * 10 + i

    return num

def reverse_list(head):
    if head is None:
        return None
    prev, cur, next = None, head, head.next
    while next:
        cur.next = prev
        prev = cur
        cur = next
        next = next.next
    cur.next = prev
    return cur
        
def sum_list_follow_up(head1, head2):
    # Reverse lists
    head1 = reverse_list(head1)
    head2 = reverse_list(head2)
    # Call sum_list
    head1 = sum_list(head1, head2)
    # Reverse list representing the sum
    return reverse_list(head1)