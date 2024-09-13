from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while i <= memory1 or i <= memory2:
            if memory1 >= memory2 and i <= memory1:
                memory1 -= i
            elif i <= memory2:
                memory2 -= i
            else:
                break
            i += 1
        return [i, memory1, memory2]
'''


'''