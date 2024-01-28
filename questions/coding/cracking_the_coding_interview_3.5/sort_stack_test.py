from sort_stack_solution import Stack

import pytest

@pytest.fixture()
def stack():
    return Stack()

# Push edge conditions
# Stack is empty.
def test_push_empty(stack):
    stack.push(0)
    assert stack.top.value == 0

# New value is the smalles (so it's on top of the stack).
def test_push_new_smallest(stack):
    stack.push(1)
    stack.push(0)
    assert stack.top.value == 0

# New value is in middle.
def test_push_value_in_middle(stack):
    expectations = [0, 5, 10]
    stack.push(10)
    stack.push(0)
    stack.push(5)

    for expected in expectations:
        assert stack.pop() == expected    

# New value is greatest (so is should be at the bottom of the stack).
def test_push_new_max(stack):
    expectations = [0, 1]
    stack.push(0)
    stack.push(1)

    for expected in expectations:
        assert stack.pop() == expected    

def test_pop(stack):
    stack.push(0)

    assert stack.pop() == 0 and stack.top is None

def test_peek(stack):
    stack.push(0)

    assert stack.peek() == 0 and stack.top

def test_is_empty(stack):
    assert stack.is_empty()

    stack.push(0)

    assert not stack.is_empty()