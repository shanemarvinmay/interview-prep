from algorithms_data_structures.sorting.bubble_sort import bubble_sort
from algorithms_data_structures.sorting.selection_sort import selection_sort


def test_bubble_sort():
    ar = [64, 34, 25, 12, 22, 11, 90, 5]

    bubble_sort(ar)

    assert ar == [5, 11, 12, 22, 25, 34, 64, 90]

def test_selection_sort():
    ar = [64, 34, 25, 12, 22, 11, 90, 5]

    selection_sort(ar)

    assert ar == [5, 11, 12, 22, 25, 34, 64, 90]
