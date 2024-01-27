class Queue:
    def __init__(self):
        self.stack = []

    def add(self, value):
        self.stack.append(value)

    def remove(self):
        rev_stack = []

        while self.stack:
            rev_stack.append(self.stack.pop())

        if len(rev_stack):
            value = rev_stack.pop()
        
        while rev_stack:
            self.stack.append(rev_stack.pop())

        return value
