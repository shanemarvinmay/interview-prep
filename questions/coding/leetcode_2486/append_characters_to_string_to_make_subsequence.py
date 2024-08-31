class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        furthest_idx_found = 0
        for ltr in s:
            if furthest_idx_found >= len(t): break
            if ltr == t[furthest_idx_found]:
                furthest_idx_found += 1
        return len(t) - furthest_idx_found
