from loop_detection_solution import loop_detection

import pytest
class Node:
    '''Single and doubly linked list node.'''
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

@pytest.fixture()
def linked_list():
    linked_list = Node(0)
    linked_list.next = Node(1)
    linked_list.next.next = Node(2)
    return linked_list

def test_loop_detection_no_loop(linked_list):
    assert loop_detection(linked_list) is None

def test_loop_detection_loop(linked_list):   
    loop_start = Node(-1)
    loop_start.next = linked_list
    # Connecting tail of linked list back to the loop start.
    itr = linked_list
    while itr.next:
        itr = itr.next
    itr.next = loop_start

    assert loop_detection(linked_list) == loop_start

