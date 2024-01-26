# Attempt 1
class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, value):
        self.stack.append(value)

        if len(self.min_stack) < 1 or value < self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self):
        if len(self.stack) < 1:
            return
        
        value = self.stack.pop()

        if value == self.min_stack[-1]:
            self.min_stack.pop()
        
        return value

    def get_min(self):
        if len(self.min_stack) < 1:
            return
        return self.min_stack[-1]


# Attempt 0 * pop failed to be O(1) *
# class Stack:
#     def __init__(self):
#         self.stack = []
#         self.min = None
    
#     def push(self, value):
#         self.stack.append(value)

#         if self.min is None or value < self.min:
#             self.min = value
    
#     def pop(self):
#         value = self.stack.pop()

#         if value == self.min:
#             self.min = min(self.stack)
        
#         return value

#     def get_min(self):
#         return self.min