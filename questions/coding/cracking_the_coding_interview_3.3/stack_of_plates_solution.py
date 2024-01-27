class SetOfStacks:
    def __init__(self):
        self.stacks = [[]]
        self.stack_limit = 10

    def push(self, value):
        if len(self.stacks[-1]) >= self.stack_limit:
            self.stacks.append([value])
        else:
            self.stacks[-1].append(value)

    def pop(self):
        # Checking if the last stack is empty.
        if len(self.stacks[-1]) == 0 and len(self.stacks) > 1:
            self.stacks.pop()
        if len(self.stacks[-1]):
            return self.stacks[-1].pop()      

    def pop_at(self, idx):
        try:
            return self.stacks[idx].pop()
        except IndexError:
            return None