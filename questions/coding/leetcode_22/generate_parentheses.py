from typing import List

class Solution:
    def __init__(self):
        self.n_answer = dict()
    def generateParenthesis(self, n: int) -> List[str]:
        if n in self.n_answer:
            return self.n_answer
        answer = []
        self.helper(n, open_count=1, close_count=0, cur=['('], options=answer)
        self.n_answer[n] = answer
        return answer
    def helper(self, n, open_count, close_count, cur, options):
        if len(cur) == 2 * n:
            options.append(''.join(cur))

        # ( if able.
        if open_count + 1 <= n:
            nxt = cur[:]
            nxt.append('(')
            self.helper(n, open_count+1, close_count, nxt, options)
        
        # ) if able.
        if close_count < open_count:
            nxt = cur[:]
            nxt.append(')')
            self.helper(n, open_count, close_count+1, nxt, options)
