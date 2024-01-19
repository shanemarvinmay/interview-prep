from partition_solution import partition_linked_list

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

def assert_partitions(less, equal_greater, partition):
    while less:
        assert less.value < partition
        less = less.next
    while equal_greater:
        assert equal_greater.value >= partition
        equal_greater = equal_greater.next

# Edge cases 

# all less than partition
def test_partition_linked_list_all_values_less():
    ll = list_to_linked_list([0, 1, 2])
    partition = 3

    less, equal_greater = partition_linked_list(ll, partition)

    assert_partitions(less, equal_greater, partition)

# all greater than or equal to partition
def test_partition_linked_list_all_values_equal_greater():
    ll = list_to_linked_list([0, 1, 2])
    partition = 0

    less, equal_greater = partition_linked_list(ll, partition)
    
    assert_partitions(less, equal_greater, partition)

# normal case
def test_partition_linked_list_normal_case():
    ll = list_to_linked_list([2, 1, 0])
    partition = 1

    less, equal_greater = partition_linked_list(ll, partition)
    print('less list')
    itr = less
    while itr:
        print(itr.value, end='->')
        itr = itr.next
    print()
    print('equal_greater')
    itr = equal_greater
    while itr:
        print(itr.value, end='->')
        itr = itr.next

    assert_partitions(less, equal_greater, partition)

# empty list
def test_partition_linked_list_empty_list():
    less, equal_greater = partition_linked_list(None, 0)

    assert less is None
    assert equal_greater is None

