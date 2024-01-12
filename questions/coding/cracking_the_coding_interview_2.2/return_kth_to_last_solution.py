def return_kth_to_last(head, k):        
    if head is None:
        return None
    # Find out how many nodes.
    num_nodes = 0
    itr = head
    while itr.next:
        num_nodes += 1
        itr = itr.next
 
    # Making sure k isn't out of range 
    if k < 0 or k > num_nodes:
        return None
    
    # Find the kth to the last node.
    itr = head
    while num_nodes > k:
        num_nodes -= 1
        itr = itr.next
    
    return itr

    # Their answer
    # current = runner = head
    # # Creating k distance between current and runner
    # for _ in range(k):
    #     if runner is None:
    #         return runner
    #     runner = runner.next
    # # Current will be the kth to the last node when runner is None
    # while runner:
    #     current = current.next
    #     runner = runner.next
    
    # return current