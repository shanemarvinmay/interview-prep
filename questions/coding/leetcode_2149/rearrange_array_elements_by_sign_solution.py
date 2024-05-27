from typing import List

class Solution:
	def rearrangeArray(self, nums: List[int]) -> List[int]:
		positives, negatives = [], []

		for num in nums:
			if num < 0:
				negatives.append(num)
			else:
				positives.append(num)
		
		return [num for tuple in zip(positives, negatives) for num in tuple]
