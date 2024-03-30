class Solution:
    def findGCD(self, nums: list[int]) -> int:
        smallest = min(nums)
        biggest = max(nums)

        gcd = 1
        for divisor in range(1, smallest + 1):
            if smallest % divisor == 0 and biggest % divisor == 0:
                gcd = divisor
        
        return gcd