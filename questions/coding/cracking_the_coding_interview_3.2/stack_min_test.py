from stack_min_solution import Stack

def test_push_min():
    stack = Stack()

    assert stack.get_min() is None

    stack.push(10)

    assert stack.get_min() == 10

    stack.push(5)

    assert stack.get_min() == 5

def test_pop_min():
    stack = Stack()

    stack.push(1)
    stack.push(0)

    assert stack.get_min() == 0

    stack.pop()

    assert stack.get_min() == 1
