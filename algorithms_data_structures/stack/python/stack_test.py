from stack import Stack

def test_push_pop():
    stack = Stack()

    for value in range(5):
        stack.push(value)

    for expected in range(4, -1, -1):
        assert stack.pop() == expected
    
    assert stack.pop() is None

def test_peek():
    stack = Stack()

    assert stack.peek() is None

    stack.push(0)

    assert stack.peek() == 0 and not stack.is_empty()

def test_is_empty():
    stack = Stack()

    assert stack.is_empty()

    stack.push(0)

    assert not stack.is_empty()