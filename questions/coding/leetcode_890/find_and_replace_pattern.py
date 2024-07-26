from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matches = []

        for word in words:
            pattern_to_word = dict()
            word_to_pattern = dict()
            matched = True
            for i in range(len(pattern)):
                if pattern[i] not in pattern_to_word:
                    pattern_to_word[pattern[i]] = word[i]
                if word[i] not in word_to_pattern:
                    word_to_pattern[word[i]] = pattern[i]
                
                if pattern_to_word[pattern[i]] != word[i] or word_to_pattern[word[i]] != pattern[i]:
                    matched = False
                    break
            if matched:
                matches.append(word)
        
        return matches