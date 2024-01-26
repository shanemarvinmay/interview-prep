class ThreeInOne:
    '''Implementing 3 stacks in one list.'''
    def __init__(self):
        self.stacks = [[],[],[]]
    
    def push(self, stack_num, value):
        self.stacks[stack_num].append(value)
    
    def pop(self, stack_num):
        return self.stacks[stack_num].pop()

    def peek(self, stack_num):
        return self.stacks[stack_num][-1]
    
    def is_empty(self, stack_num):
        return len(self.stacks[stack_num]) < 1