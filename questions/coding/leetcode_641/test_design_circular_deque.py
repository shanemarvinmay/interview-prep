from questions.coding.leetcode_641.design_circular_deque import MyCircularDeque

def test_MyCircularDeque():
    myCircularDeque = MyCircularDeque(3)
    assert myCircularDeque.insertLast(1) # return True
    assert myCircularDeque.insertLast(2) # return True
    assert myCircularDeque.insertFront(3)  # return True
    assert myCircularDeque.insertFront(4) == False  # return False, the queue is full.
    assert myCircularDeque.getRear() == 2     # return 2
    assert myCircularDeque.isFull()      # return True
    assert myCircularDeque.deleteLast()  # return True
    assert myCircularDeque.insertFront(4)  # return True
    assert myCircularDeque.getFront() == 4    # return 4
