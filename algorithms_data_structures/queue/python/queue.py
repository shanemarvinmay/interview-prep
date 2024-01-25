class Queue:
    '''This is the Queue class implemented in python with nodes.'''
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
        
    def __init__(self):
        self.start = None
        self.end = None

    def add(self, value):
        node = self.Node(value)
        # Queue is empty
        if self.start is None:
            self.start = node
            self.end = node
        # 1 or more elements in queue
        else:
            self.end.next = node
            self.end = node

    def remove(self):
        # Queue is empty.
        if self.start is None:
            return None
        value = self.start.value
        # Only 1 node in queue.
        if self.start == self.end:
            self.end = None
        # 1 or more nodes in queue.
        self.start = self.start.next

        return value

    def peek(self):
        if self.start:
            return self.start.value

    def is_empty(self):
        return self.start is None