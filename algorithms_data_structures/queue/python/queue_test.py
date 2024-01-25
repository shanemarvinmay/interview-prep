from queue import Queue

def test_add_remove():
    q = Queue()

    for value in range(5):
        q.add(value)
    
    for value in range(5):
        assert q.remove() == value

    assert q.remove() is None

def test_peek():
    q = Queue()

    assert q.peek() is None

    q.add(0)

    assert q.peek() == 0 and not q.is_empty()

def test_is_empty():
    q = Queue()

    assert q.is_empty()

    q.add(0)

    assert not q.is_empty()
