from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ks = []
        max_limit = 2 ** maximumBit

        while nums:
            max_xor = 0
            max_k = 0
            for k in range(max_limit):
                xor = self.get_xor(k, nums)
                if xor > max_xor:
                    max_xor = xor
                    max_k = k
                if max_xor == max_limit - 1:
                    break
            ks.append(max_k)
            nums.pop()
        
        return ks
    def get_xor(self, k, nums):
        xor = k
        for num in nums:
            xor ^= num
        return xor
