from collections import deque

class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted_string = deque()

        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                # The 2 chars before are the number.
                num = int(s[i-2 : i])
                # 97 is a, 122 is z
                ltr = chr(num + 96)
                decrypted_string.appendleft(ltr)
                i -= 3
            else:
                num = int(s[i])
                ltr = chr(num + 96)
                decrypted_string.appendleft(ltr)
                i -= 1
        
        return ''.join(decrypted_string)