from three_in_one_solution import ThreeInOne

import pytest

def test_push_pop_not_empty():
    three_in_one = ThreeInOne()

    three_in_one.push(0, 0)

    assert three_in_one.pop(0) == 0 and three_in_one.is_empty(0)

def test_pop_empty():
    three_in_one = ThreeInOne()

    with pytest.raises(IndexError):
        three_in_one.pop(0)

def test_push_peek_not_empty():
    three_in_one = ThreeInOne()

    three_in_one.push(0, 0)

    assert three_in_one.peek(0) == 0 and not three_in_one.is_empty(0)

def test_peek_empty():
    three_in_one = ThreeInOne()

    with pytest.raises(IndexError):
        three_in_one.peek(0)
