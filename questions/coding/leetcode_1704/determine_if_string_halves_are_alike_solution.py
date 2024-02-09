class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left_vowel_count = right_vowel_count = 0
        left_idx, right_idx = 0, len(s) // 2

        while right_idx < len(s):
            left_vowel_count = left_vowel_count + 1 if s[left_idx] in vowels else left_vowel_count
            right_vowel_count = right_vowel_count + 1 if s[right_idx] in vowels else right_vowel_count
            
            left_idx += 1
            right_idx += 1

        return left_vowel_count == right_vowel_count
