class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        total = 0
        length = len(nums)

        for i in range(1, len(nums) + 1):
            if length % i == 0:
                total += nums[i - 1] ** 2

        return total
