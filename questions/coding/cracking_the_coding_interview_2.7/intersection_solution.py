def intersection(head1, head2):
    nodes_seen = set()

    itr = head1
    while itr:
        nodes_seen.add(itr)
        itr = itr.next
    
    itr = head2
    while itr:
        if itr in nodes_seen:
            return itr
        itr = itr.next
    
    return None