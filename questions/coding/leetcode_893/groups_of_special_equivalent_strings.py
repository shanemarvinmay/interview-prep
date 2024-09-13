from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        # {even_ltrs (sorted) + odd_ltrs (sorted) , }
        groups = set()
        num_groups = 0
        for word in words:
            group = self.get_group(word)
            if group not in groups:
                num_groups += 1
                groups.add(group)
        return num_groups
    def get_group(self, word):
        evens, odds = [], []
        for i in range(len(word)):
            if i % 2:
                odds.append(word[i])
            else:
                evens.append(word[i])
        evens.sort()
        evens = ''.join(evens)
        odds.sort()
        odds = ''.join(odds)
        return f"{evens}{odds}"
