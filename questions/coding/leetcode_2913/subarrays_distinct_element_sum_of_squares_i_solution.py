class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        # Getting counts of unique numbers in each subarray.
        unique_nums_counts = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                unique_nums_count = len(set(nums[i:j]))
                unique_nums_counts.append(unique_nums_count)
        
        # Summing up the squares.
        sum_squares = 0
        for unique_nums_count in unique_nums_counts:
            sum_squares += unique_nums_count ** 2

        return sum_squares
