from typing import List
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        num_pairs = 0

        for num1 in nums1:
            for num2 in nums2:
                divisor = num2 * k
                if num1 // divisor == num1 / divisor:
                    num_pairs += 1
        
        return num_pairs
