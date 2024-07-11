from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output = []
        num = 1
        idx = 0

        while idx < len(target):
            output.append('Push')
            if num == target[idx]:
                idx += 1
            else:
                output.append("Pop")
            num += 1
    
        return output
