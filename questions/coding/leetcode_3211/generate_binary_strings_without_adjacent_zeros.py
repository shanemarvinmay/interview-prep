from typing import List

class Solution:
    def validStrings(self, n: int) -> List[str]:
        output = []

        for i in range(2**n):
            binary = format(i, f'0{n}b')
            if '00' in binary:
                continue
            output.append(binary)

        return output
