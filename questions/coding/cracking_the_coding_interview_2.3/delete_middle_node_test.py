import pytest

from delete_middle_node_solution import delete_middle_node

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

def get_middle_node(head):
    '''Returns middle node is the number of nodes is odd. 
    If the number of nodes is even, it returns the rightmost middle node.'''
    slow, fast = head, head.next
    while fast:
        slow = slow.next
        if fast.next is None or fast.next.next is None:
            break
        fast = fast.next.next
    return slow

def assert_linked_list_are_equal(l1, l2):
    p1, p2 = l1, l2
    while p1 and p2:
        print(f'p1:{p1.value}\tp2:{p2.value}')
        assert p1.value == p2.value
        p1 = p1.next
        p2 = p2.next
    if p1:
        print(f'p1:{p1.value}')
    if p2:
        print(f'p2:{p2.value}')
    assert p1 is None and p2 is None

def test_delete_middle_node_single_node():
    node = expected = Node(0)

    delete_middle_node(node)

    assert node.value == expected.value

def test_delete_middle_node_even_length():
    linked_list = list_to_linked_list([0, 0, 1, 0])
    expected = list_to_linked_list([0, 0, 0])
    middle_node = get_middle_node(linked_list)

    delete_middle_node(middle_node)

    assert_linked_list_are_equal(linked_list, expected)

def test_delete_middle_node_even_length():
    linked_list = list_to_linked_list([0, 0, 1, 0, 0])
    expected = list_to_linked_list([0, 0, 0, 0])
    middle_node = get_middle_node(linked_list)

    delete_middle_node(middle_node)

    assert_linked_list_are_equal(linked_list, expected)

@pytest.mark.parametrize("test_input,expected", [
    (list_to_linked_list([0, 1]), list_to_linked_list([0, 1])),
    (Node(0), Node(0))])
def test_delete_middle_node_no_mid(test_input, expected):
    '''The problem says not to delete the first of last nodes.'''
    middle_node = get_middle_node(test_input)
    
    delete_middle_node(middle_node)

    assert_linked_list_are_equal(test_input, expected)
 