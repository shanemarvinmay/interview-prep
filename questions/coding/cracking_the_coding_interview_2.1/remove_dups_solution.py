 # single and doubly linked list
class Node:
    '''Node that can be used for single or double linked list.'''
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
def list_to_linked_list(l):
    if len(l) < 0:
        return
    
    head = Node(l[0])
    itr = head
    for i in range(1, len(l)):
        itr.next = Node(l[i])
        itr = itr.next
    
    return head


def remove_dups(head):
    if head is None or head.next is None:
        return head
    # O(n)
    # seen_values = set([head.value])
    # p1, p2 = head, head.next

    # while p2 is not None:
    #     # Remove value if it's been seen before
    #     if p2.value in seen_values:
    #         p1.next = p2.next
    #         p2 = p1.next
    #     else:
    #         seen_values.add(p2.value)
    #         p1 = p1.next
    #         p2 = None if p1 is None else p1.next

    # Follow up
    slow, fast_0, fast_1 = head, head, head.next
    while slow != fast_1:
        if slow.value == fast_1.value:
            # Head
            if head == fast_1:
                head = head.next
            # Mid or end
            else:
                fast_0.next = fast_1.next
        # Slow moves 1 node and Fast moves 2 node
        slow = head if slow.next is None else slow.next
        fast_0 = head if fast_1.next is None else fast_1.next
        fast_1 = head if fast_0.next is None else fast_0.next
    
    return head