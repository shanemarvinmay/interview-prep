def delete_middle_node(node):
    if node is None or node.next is None:
        return
    prev = node
    itr = node.next

    while itr.next:
        prev.value = itr.value
        prev = itr
        itr = itr.next
    
    # Deleting the last node.
    prev.value = itr.value
    prev.next = None
