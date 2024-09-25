class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bg = 0
        vowels = 'aeiou'
        mask = 0
        state_first_occurance = {0:-1}
        for idx, ltr in enumerate(s):
            vowel_idx = vowels.find(ltr)
            if vowel_idx > -1:
                vowel_bit = 2**vowel_idx
                mask ^= vowel_bit
            if mask in state_first_occurance:
                even_length = idx - state_first_occurance[mask]
                bg = max(bg, even_length)
            else:
                state_first_occurance[mask] = idx
        return bg

'''
1371. Find the Longest Substring Containing Vowels in Even Counts
https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/
'''