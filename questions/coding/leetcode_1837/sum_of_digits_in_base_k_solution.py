class Solution:
    def sumBase(self, num: int, base: int) -> int:
        total = 0

        while num > 0:
            total += num % base

            num = num // base
        
        return total
