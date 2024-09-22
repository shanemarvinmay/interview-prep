class Solution:
    def stringHash(self, s: str, k: int) -> str:
        # 'a': 97
        # ...
        # 'z': 122
        output = []
        for i in range(0, len(s), k):
            # Getting sum of substring
            total = 0
            for j in range(i, i+k):
                # Letter to index
                total += (ord(s[j]) - 97)
            # Remainder of 26
            total %= 26
            # Total to number
            output.append(chr(total+97))
        return ''.join(output)
