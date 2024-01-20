def palindrome(head):
    itr = head
    unique_values = set()
    while itr:
        if itr.val in unique_values:
            unique_values.remove(itr.val)
        else:
            unique_values.add(itr.val)
        itr = itr.next
    return len(unique_values) <= 1
