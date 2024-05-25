class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        diff = 0

        ltr_to_idx = dict()
        for i in range(len(s)):
            ltr_to_idx[s[i]] = i
        
        for i in range(len(t)):
            diff += abs(i - ltr_to_idx[t[i]])
        
        return diff
