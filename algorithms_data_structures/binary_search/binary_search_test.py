from algorithms_data_structures.binary_search.binary_search import binary_search

import pytest

@pytest.mark.parametrize('ar, target, expected, message', [
    ([0,1,2,3,4,5,6,7,8,9], 7, 7, 'Need to go right then left - found'),
    ([0,1,2,3,4,5,6,7,8,9], 10, -1, 'Too big - not found'),
    ([0,1,2,3,4,5,6,7,8,9], -2, -1, 'Too small - not found'),
    ([0,1,2,3,4,5,6,7,8,9], 7.5, -1, 'Need to go right then left - not found'),
])
def test_binary_search(ar, target, expected, message):
    got = binary_search(ar, target)

    assert got == expected, message
