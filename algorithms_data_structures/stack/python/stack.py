class Stack:
    '''This is the Stack classed implement in python with nodes.

    Nodes are being used here since the list (vector) implementation is already done in python.'''

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.top = None
    
    def push(self, value):
        # Stack is empty.
        if self.top is None:
            self.top = self.Node(value)
        else:
            node = self.Node(value)
            node.next = self.top
            self.top = node

    def pop(self):
        # Stack is empty
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        # Stack is empty.
        if self.top is None:
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None