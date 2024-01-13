from return_kth_to_last_solution import return_kth_to_last

 # Single and doubly linked list
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

linked_list = list_to_linked_list([1, 2, 3])

# Head is none
def test_return_kth_to_last_head_is_none():
    assert return_kth_to_last(None, 0) is None

# k is head
def test_return_kth_to_last_return_head():
    got = return_kth_to_last(linked_list, 2)

    assert got.value == 1

# k is middle
def test_return_kth_to_last_return_mid_node():
    got = return_kth_to_last(linked_list, 1)

    assert got.value == 2

# k is last element
def test_return_kth_to_last_return_end():
    got = return_kth_to_last(linked_list, 0)

    assert got.value == 3

# k is out of range
def test_return_kth_to_last_k_is_out_range():
    assert return_kth_to_last(linked_list, -1) is None
    assert return_kth_to_last(linked_list, 3) is None