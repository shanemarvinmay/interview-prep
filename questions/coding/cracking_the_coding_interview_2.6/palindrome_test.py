from palindrome_solution import palindrome

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

@pytest.fixture(scope='module')
def odd_length_palindrome_linked_list():
    return list_to_linked_list([0, 1, 0])

@pytest.fixture(scope='module')
def odd_length_linked_list():
    return list_to_linked_list([0, 1, 2])

@pytest.fixture(scope='module')
def even_length_palindrome_linked_list():
    return list_to_linked_list([0, 1, 1, 0])

@pytest.fixture(scope='module')
def even_length_linked_list():
    return list_to_linked_list([0, 1, 2, 0])


@pytest.mark.parametrize('fixture, expected', [
    ("odd_length_palindrome_linked_list", True),
    ("odd_length_linked_list", False),
    ("odd_length_palindrome_linked_list", True),
    ("even_length_linked_list", False)])
def test_palindrome(fixture, expected, request):
    linked_list = request.getfixturevalue(fixture)

    assert palindrome(linked_list) == expected





''' 
Edge cases
odd / even length
palindrome vs not
empty ?
'''