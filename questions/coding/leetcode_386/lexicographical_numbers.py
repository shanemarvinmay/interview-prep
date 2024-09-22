from typing import List

'''
You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
1 <= n <= 5 * 104
'''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        output = []
        def helper(cur, str_n):
            if len(cur) >= len(str_n): return
            for i in range(10):
                cur.append(f"{i}")
                num = ''.join(cur)
                if int(num) > n:
                    cur.pop() 
                    return
                output.append(num)
                helper(cur, str_n)
                cur.pop()
        
        for i in range(1, 10):
            if i > n: break
            digit = f"{i}"
            output.append(digit)
            helper(cur=[digit], str_n=f"{n}")

        output = [int(num) for num in output]
        
        return output
