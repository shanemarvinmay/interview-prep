class Solution:
    def generateTheString(self, n: int) -> str:
        output = ['a'] * n

        if n % 2 == 0:
            output.pop()
            output.append('b')
        
        return ''.join(output)
