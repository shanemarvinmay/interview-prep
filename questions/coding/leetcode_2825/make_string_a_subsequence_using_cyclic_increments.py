class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1): return False
        i = j = 0
        while j < len(str2):
            num2 = ord(str2[j])
            j += 1
            changed = False
            while i < len(str1) and not changed:
                num1 = ord(str1[i])
                i += 1
                if num1 != num2:
                    num1 = num1 + 1 if num1 < 122 else 97
                if num1 == num2:
                    changed = True
            if not changed: return False
        return True