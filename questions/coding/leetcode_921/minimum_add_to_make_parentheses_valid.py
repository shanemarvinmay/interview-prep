class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        changes = 0
        opens = 0
        for i in s:
            if i == '(':
                opens += 1
            else:
                opens -= 1
            if opens < 0:
                changes += 1
                opens = 0
        changes += opens
        return changes
