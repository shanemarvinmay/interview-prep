class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            # Getting the last bits.
            a_bit, b_bit, c_bit = a%2, b%2, c%2
            # Getting rid of last bit in nums.
            a, b, c = a//2, b//2, c//2
            # Checking how many flips we may have to take.
            if (a_bit | b_bit) == c_bit:
                continue
            elif c_bit == 0:
                flips += a_bit + b_bit
            else:
                flips += 1
        return flips
