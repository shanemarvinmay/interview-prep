class Solution:
    def __init__(self):
        self.vowels = ['a','e','i','o','u']
        self.count = 0
    def countVowelStrings(self, n: int) -> int:
        self.count = 0
        self.get_string_count(n)
        return self.count
    def get_string_count(self, n, s=None):
        if s is None:
            s = ''
        if len(s) == n:
            self.count += 1
            return
        for vowel in self.vowels:
            if len(s) == 0 or s[-1] <= vowel:
                self.get_string_count(n, f'{s}{vowel}')
