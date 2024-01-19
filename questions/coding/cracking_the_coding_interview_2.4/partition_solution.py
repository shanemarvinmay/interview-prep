def partition_linked_list(head, partition):
    if head is None:
        return None, None
    
    equal_greater = head
    less = None
    while equal_greater:
        # Fiding the first/next node that is equal or greater than the partition.
        while equal_greater and equal_greater.value < partition:
            equal_greater = equal_greater.next
        if equal_greater and less is None:
            less = equal_greater.next
        # Fiding the next node after equal_greater that is less than the partition.
        while less and less.value >= partition:
            less = less.next
        
        if less is None or equal_greater is None:
            break
        # Swap
        temp = equal_greater.value
        equal_greater.value = less.value
        less.value = temp
        
        equal_greater = equal_greater.next
    
    # All nodes < partition
    if equal_greater is None and less is None:
        return head, None
    
    if equal_greater == head:
        return None, equal_greater
    
    # Finding the head of the right.
    itr = head
    while itr.next and itr.next.value < partition:
        itr = itr.next
        
    equal_greater_head = itr.next
    itr.next = None

    return head, equal_greater_head
