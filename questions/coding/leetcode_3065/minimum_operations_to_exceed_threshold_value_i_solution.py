import heapq

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        num_operations = 0
        heapq.heapify(nums)
        
        while len(nums) and heapq.heappop(nums) < k:
            num_operations += 1
        
        return num_operations