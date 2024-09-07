from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        changes = 0
        c = Counter(s)
        for ltr in t:
            if ltr not in c or c[ltr] <= 0:
                changes += 1
            else:
                c[ltr] -= 1
        for ltr, freq in c.items():
            if freq <= 0: continue
            changes += freq
        return changes
