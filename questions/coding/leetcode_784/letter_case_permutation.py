from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s = s.lower()
        ltrs = list(s)
        strs = set()
        self.helper(ltrs, idx=0, seen=strs)
        return list(strs)
    def helper(self, ltrs, idx, seen):
        if idx == len(ltrs):
            return
        if ltrs[idx].isnumeric():
            seen.add(''.join(ltrs))
            return self.helper(ltrs, idx+1, seen)
        
        cp = ltrs[:]
        cp[idx] = cp[idx].upper()

        seen.add(''.join(ltrs))
        seen.add(''.join(cp))

        self.helper(ltrs, idx+1, seen)
        self.helper(cp, idx+1, seen)
