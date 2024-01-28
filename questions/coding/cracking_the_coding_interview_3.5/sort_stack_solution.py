class Stack:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.top = None
    
    def push(self, value):
        new_node = self.Node(value)
        # Stack is empty.
        if self.top is None:
            self.top = new_node
            return
        # If value needs to be new head.
        if value < self.top.value:
            new_node.next = self.top
            self.top = new_node
            return
        # Find place for new value (might be bottom).
        itr = self.top
        while itr.next and itr.next.value < value:
            itr = itr.next
        new_node.next = itr.next
        itr.next = new_node


    def pop(self):
        if self.top is None:
            return
        value = self.top.value
        self.top = self.top.next
        return value


    def peek(self):
        if self.top is None:
            return
        return self.top.value

    def is_empty(self):
        return self.top is None