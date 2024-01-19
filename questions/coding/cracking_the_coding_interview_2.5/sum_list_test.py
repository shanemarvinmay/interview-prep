from sum_list_solution import *

import pytest

@pytest.fixture()
def example_list():
    '''2 -> 0 -> 1'''
    head = Node(2)
    head.next = Node(0)
    head.next.next = Node(1)
    return head

def test_sum_list_empty_list():
    got =  sum_list(Node(1), None)
    assert got.val == 1

    got = sum_list(None, Node(1))
    assert got.val == 1

    got = sum_list(None, None)
    assert got is None

# Carry over, diff lengths, more digits needed
def test_test_sum_list_carry_over():
    # 999
    list1 = Node(9)
    list1.next = Node(9)
    list1.next.next = Node(9)

    # 99
    list2 = Node(9)
    list2.next = Node(9)

    got_list = sum_list(list1, list2)
    got_num = list_to_num(got_list)

    assert got_num == 1098

def test_list_to_num(example_list):
    assert list_to_num(None) == 0
    assert list_to_num(example_list) == 102

def test_reverse_list(example_list):
    expected = Node(1)
    expected.next = Node(0)
    expected.next.next = Node(2)

    got = reverse_list(example_list)

    assert list_to_num(got) == list_to_num(expected)
    assert list_to_num(reverse_list(Node(1))) == list_to_num(Node(1))
    assert reverse_list(None) is None

def test_sum_list_follow_up_carry_over():
    # 1098
    expected = Node(1)
    expected.next = Node(0)
    expected.next.next = Node(9)
    expected.next.next.next = Node(8)
    # 999
    list1 = Node(9)
    list1.next = Node(9)
    list1.next.next = Node(9)
    # 99
    list2 = Node(9)
    list2.next = Node(9)

    got = sum_list_follow_up(list1, list2)

    while got and expected:
        print(got.val, expected.val)
        assert got.val == expected.val
        got = got.next
        expected = expected.next
    assert got is None and expected is None