from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Max is 10_000_000 which needs more then 23 bits
        bits_count = [0] * 24

        for candidate in candidates:
            bits = bin(candidate)
            bit_idx = -1
            for i in range(len(bits)-1, 1, -1):
                if bits[i] == '1':
                    bits_count[bit_idx] += 1
                bit_idx -= 1
        
        return max(bits_count)
