class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0

        for word in words:
            pref_len = len(pref)
            if len(word) >= pref_len and word[:pref_len] == pref:
                count += 1
        
        return count
