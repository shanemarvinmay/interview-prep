import heapq

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        total = 0
        # O(n)
        heapq._heapify_max(nums)
        # 1 / 2 nums len
        while nums:
            # 2 log(nums len)
            max_1, max_2 = heapq._heappop_max(nums), heapq._heappop_max(nums)
            total += min(max_1, max_2)
        
        return total