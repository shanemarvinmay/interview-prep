from typing import List

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        changes = 0
        unique_smaller = set()
        nums.sort()
        smallest = nums[0]
        
        for i in range(len(nums)):
            if nums[i] > smallest:
                if nums[i] in unique_smaller:
                    unique_smaller.remove(nums[i])
                changes += len(unique_smaller)
            unique_smaller.add(nums[i])
        
        return changes
'''
1887. Reduction Operations to Make the Array Elements Equal
https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
Input: nums = 
Explanation: It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [3,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [1,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1].
Example 2:

Input: nums = 
Explanation: All elements in nums are already equal.
Example 3:

Input: nums = 
'''