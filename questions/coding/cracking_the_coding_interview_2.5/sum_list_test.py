from sum_list_solution import *

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
    
    itr = got_list
    while itr:
        print(itr.val)
        itr = itr.next

    assert got_num == 1098

def test_list_to_num():
    assert list_to_num(None) == 0

    # 102
    input_list = Node(2)
    input_list.next = Node(0)
    input_list.next.next = Node(1)
    assert list_to_num(input_list) == 102
