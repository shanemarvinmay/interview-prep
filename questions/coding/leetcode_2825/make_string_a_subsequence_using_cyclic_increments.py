class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1): return False
        # Making map of str2
        str2_map = dict()
        for ltr in str2:
            num = ord(ltr)
            if num not in str2_map:
                str2_map[num] = 1
            str2_map[num] += 1
        # Checking if we can make every letter in str2 from str1
        for ltr in str1:
            num = ord(ltr)
            if num in str2_map:
                str2_map[num] -= 1
            
        return True
