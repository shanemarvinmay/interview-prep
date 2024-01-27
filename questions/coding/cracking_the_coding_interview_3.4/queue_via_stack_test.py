from queue_via_stack import Queue

def test_add():
    q = Queue()

    for i in range(5):
        q.add(i)

    assert q.stack == [0, 1, 2, 3, 4]

def test_remove():
    q = Queue()

    for i in range(5):
        q.add(i)

    for i in range(0):
        assert q.remove() == i