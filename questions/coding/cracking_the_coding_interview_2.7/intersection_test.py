from intersection_solution import intersection
from random import randint

import pytest


class Node:
    '''Single and doubly linked list node.'''
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def list_to_linked_list(l):
    if len(l) < 1:
        return None
    
    head = Node(l[0])
    itr = head
    for i in range(1, len(l)):
        itr.next = Node(l[i])
        itr = itr.next
    
    return head

@pytest.fixture()
def empty_list():
    return None

@pytest.fixture()
def random_list():
    '''Generate a list of random letters from A to Z.
    
    Letters A to Z are represented by the numbers 65 to 90 inclusively.'''
    length = randint(1, 5)
    head = Node(chr(randint(65, 90)))
    itr = head
    for _ in range(length):
        itr.next = Node(chr(randint(65, 90)))
        itr = itr.next
    return head

@pytest.fixture()
def different_lists(random_list):
    return list_to_linked_list([0, 1, 2, 3]), random_list

@pytest.fixture()
def common_node():
    return Node('common')

@pytest.fixture()
def intersecting_lists(different_lists, common_node):
    head1, head2 = different_lists
    common_node = common_node

    # Adding the common node to the second position in first list.
    common_node.next = head1.next
    head1.next = common_node

    # Adding the common node to the end of the second list.
    itr = head2
    while itr.next:
        itr = itr.next
    itr.next = common_node

    return head1, head2

    

def test_intersection_something_common(intersecting_lists, common_node):
    head1, head2 = intersecting_lists
    assert intersection(head1, head2) == common_node, "2 list with a common node."

def test_intersection_nothing_common(different_lists):
    head1, head2 = different_lists
    assert intersection(head1, head2) is None, "2 non intersecting list."

@pytest.mark.parametrize('fixture1, fixture2, message', [
    ('random_list', 'empty_list', "Random and empty list."),
    ('empty_list', 'random_list', "Empty and random list."),
    ('empty_list', 'empty_list', "Empty lists.")
])
def test_intersection_at_least_one_empty(fixture1, fixture2, message, request):
    head1 = request.getfixturevalue(fixture1)
    head2 = request.getfixturevalue(fixture2)

    assert intersection(head1, head2) is None, message
