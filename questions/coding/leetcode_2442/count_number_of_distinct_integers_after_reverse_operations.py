from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        unique_nums = set()

        for num in nums:
            unique_nums.add(num)
            unique_nums.add(self.reverse(num))
        
        return len(unique_nums)

    def reverse(self, num):
        output = 0
        while num:
            digit = num % 10
            output *= 10
            output += digit
            num //= 10
        return output
