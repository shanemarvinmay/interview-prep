from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        else:
            length = n * 2 - 1
            res = [0] * length
        used = set()
        
        def backtrack(i):
            if i == length:
                return True
            # Try largest
            for num in range(n, 0, -1):
                # Validation
                if num in used:
                    continue
                if num > 1 and (i+num >= length or res[i+num]):
                    continue

                # Try decision
                used.add(num)
                res[i] = num
                if num > 1:
                    res[i+num] = num
                
                nxt = i + 1
                while nxt < length and res[nxt]:
                    nxt += 1
                
                # Recursive step
                if backtrack(nxt):
                    return True
                
                # Backtrack
                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i + num] = 0
            return False
            

        backtrack(0)
        return res
