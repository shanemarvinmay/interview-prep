from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total = 0
        # Getting frequency of each num to see what is unique.
        num_to_frequency = [0] * 101
        for num in nums:
            num_to_frequency[num] += 1

        # Adding up the unique elements.
        for num in range(len(num_to_frequency)):
            if num_to_frequency[num] == 1:
                total += num
        
        return total
