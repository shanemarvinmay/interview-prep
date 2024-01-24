def loop_detection(head):
    if head is None:
        return
    slow, fast = head, head.next

    while slow != fast and fast:
        slow = slow.next
        fast = fast.next.next if fast.next else None
    
    return fast

