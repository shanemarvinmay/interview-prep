from merge_nodes_in_between_zeros_solution import merge_nodes_in_between_zeros

import pytest

 # Single and doubly linked list
class Node:
    '''Node that can be used for single or double linked list.'''
    def __init__(self, val):
        self.val = val
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
   
def assert_linked_list_are_equal(l1, l2):
    p1, p2 = l1, l2
    while p1 and p2:
        print(f'p1:{p1.val}\tp2:{p2.val}')
        assert p1.val == p2.val
        p1 = p1.next
        p2 = p2.next
    if p1:
        print(f'p1:{p1.val}')
    if p2:
        print(f'p2:{p2.val}')
    assert p1 is None and p2 is None

@pytest.mark.parametrize("got, expected", [
    ([0,3,1,0,4,5,2,0], [4,11]),
    ([0,1,0,3,0,2,2,0], [1,3,4])])
def test_merge_nodes_in_between_zeros(got, expected):
    expected_list = list_to_linked_list(expected)
    input_list = list_to_linked_list(got)

    got_list = merge_nodes_in_between_zeros(input_list)

    assert_linked_list_are_equal(got_list, expected_list)