from typing import List
class Solution:
	def duplicateNumbersXOR(self, nums: List[int]) -> int:
		result = 0
		nums_seen = set()

		for num in nums:
			if num in nums_seen:
				result ^= num
			nums_seen.add(num)
		
		return result
