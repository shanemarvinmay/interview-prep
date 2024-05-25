from typing import List


class Solution:
	def minOperations(self, nums: List[int], k: int) -> int:
		# Attempt #1 Time O(n * num bits)
		diffs = 0

		# Get xor of nums
		xor_result = None
		for num in nums:
			if xor_result:
				xor_result = xor_result ^ num
			else:
				xor_result = num

		# Count bits that are different from k and the xor result
		xor_result_binary = bin(xor_result)[2:]
		k_binary = bin(k)[2:]

		xor_idx = len(xor_result_binary) - 1
		k_idx = len(k_binary) - 1
		while xor_idx >= 0 and k_idx >= 0:
			if xor_result_binary[xor_idx] != k_binary[k_idx]:
				diffs += 1
			xor_idx -= 1
			k_idx -= 1 
		while xor_idx >= 0:
			if xor_result_binary[xor_idx] == '1':
				diffs += 1
			xor_idx -= 1
		while k_idx >= 0:
			if k_binary[k_idx] == '1':
				diffs += 1
			k_idx -= 1 
		
		return diffs

    # Attempt #0 Time O(n * num bits)
    #     diffs = 0
    #     divisor = 1
    #     # Get binary of k <- 24 bits b/c that's the max
    #     k_binary = "{0:024b}".format(k)

    #     for i in range(len(k_binary) - 1, 0, -1):
    #         xor = self.get_xor(nums, divisor)
    #         last_xor_bit = bin(xor)[-1]
    #         k_bit = k_binary[i]
    #         if k_bit != last_xor_bit:
    #             diffs += 1
    #         divisor *= 2

    #     return diffs

    # def get_xor(self, nums: List[int], divisor: int) -> int:
    #     result = None
    #     for num in nums:
    #         if result:
    #             result = result ^ (num // divisor)
    #         else:
    #             result = num // divisor
    #     return result
