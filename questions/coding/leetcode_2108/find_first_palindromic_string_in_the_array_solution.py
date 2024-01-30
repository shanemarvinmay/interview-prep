class Solution:
    def is_palindrome(self, word):
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.is_palindrome(word):
                return word
        return ""
