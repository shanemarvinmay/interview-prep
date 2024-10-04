from collections import deque
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openers = []
        output = []
        for i in range(len(s)):
            if s[i] == '(':
                openers.append(i)
                output.append(s[i])
            elif s[i] == ')' and openers:
                openers.pop()
                output.append(s[i])
            elif s[i] not in ['(', ')']:
                output.append(s[i])
        # Taking care of extra openers
        # openers = set(openers)
        closers = []
        s = deque()
        for i in range(len(output)-1, -1, -1):
            if output[i] == '(' and closers:
                closers.pop()
                s.appendleft(output[i])
            elif output[i] == ')':
                closers.append(output[i])
                s.appendleft(output[i])
            elif output[i] not in ['(', ')']:
                s.appendleft(output[i])
        # s = []
        # for i in range(len(output)):
        #     if i not in openers:
        #         s.append(output[i])
        # output = [output[i] for i in range(len(output)) if i not in openers]
        return ''.join(s)
