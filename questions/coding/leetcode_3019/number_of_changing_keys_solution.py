class Solution:
    def countKeyChanges(self, s: str) -> int:
        key_changes = 0
        s = s.lower()
        prev_key = s[0]

        for key in s:
            if key != prev_key:
                key_changes += 1
            prev_key = key
        
        return key_changes
