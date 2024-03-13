from collections import deque
class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        perm = []
        low = 0
        high = len(s) 
        for ltr in s:
            if ltr == "I":
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1
        perm.append(high)
        
        return perm
