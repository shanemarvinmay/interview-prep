from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        ltr_to_frequency = Counter(s)

        normal_ltr_frequency = 0
        for ltr in ltr_to_frequency:
            if normal_ltr_frequency < 1:
                normal_ltr_frequency = ltr_to_frequency[ltr]
                continue
            if ltr_to_frequency[ltr] != normal_ltr_frequency:
                return False
        
        return True