class Solution:
    def find_set_mismatch(self, nums: list[int]) -> tuple[int]:
        duplicate_num, missing_num = 0, 0
        unique_nums = set()

        # Finding duplicate num
        for num in nums:
            if num in unique_nums:
                duplicate_num = num
            unique_nums.add(num)
        
        # Finding missing number
        for num in range(1, len(nums) + 1):
            if num not in unique_nums:
                missing_num = num
                break

        return duplicate_num, missing_num
