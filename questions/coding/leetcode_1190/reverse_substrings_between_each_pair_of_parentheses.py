class Solution:
    def reverseParentheses(self, s: str) -> str:
        s = list(s)
        i = len(s)-1
        while i > -1:
            # Finding last open
            while i > -1 and s[i] != '(':
                i -= 1
            if i < 0: break
            # Finding last close
            j = i + 1
            while s[j] != ')':
                j += 1
            # () to ..
            s[i], s[j] = '.', '.'
            self.reverse_between(i, j, s)
        s = [char for char in s if char != '.']
        return ''.join(s)
    def reverse_between(self, start, end, s):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
