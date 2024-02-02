class Solution:
    def minOperations(self, nums: list[int]) -> int:
        moves = 0
        cur_max = nums[0]
        
        for i in range(1, len(nums)):
            cur_max += 1
            if nums[i] <  cur_max:
                moves += abs(cur_max - nums[i])
            else:
                cur_max = nums[i]
        
        return moves