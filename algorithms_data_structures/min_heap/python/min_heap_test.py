from min_heap import MinHeap

import pytest

@pytest.mark.parametrize('input_nums, expected, message', [
    ([], [], 'Heap is empty.'),
    ([1, 0], [0, 1], 'New value is new min.'),
    ([1, 0, 2], [0, 1, 2], 'New value is max.'),
    ([10, 0, 20, 5], [0, 5, 20, 10], 'New value is inbetween min and max.')
])
def test_insert(input_nums, expected, message):
    min_heap = MinHeap()
    
    for num in input_nums:
        min_heap.insert(num)

    assert min_heap.heap == expected, message


def test_pop_min_heapify():
    min_heap = MinHeap()

    for i in range(10):
        min_heap.insert(i)
    
    for i in range(10):
        print(i, min_heap.heap)
        assert min_heap.pop_min() == i