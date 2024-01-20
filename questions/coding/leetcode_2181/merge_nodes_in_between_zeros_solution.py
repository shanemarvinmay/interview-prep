def merge_nodes_in_between_zeros(head):
    prev = next = head

    while next:
        total = 0
        # Finding the next zero.
        while next.val != 0 or next == prev:
            total += next.val
            next = next.next
        prev.val = total
        prev.next = next.next
        # Cutting out the nodes that were summed up.
        next.next = None

        prev = prev.next
        next = prev
    
    return head
