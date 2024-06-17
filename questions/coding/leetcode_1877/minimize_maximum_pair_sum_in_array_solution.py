from typing import List

def merge_sort(nums):
	if len(nums) == 1:
		return nums

	m = len(nums) // 2

	l = merge_sort(nums[:m])
	r = merge_sort(nums[m:])

	l_idx = r_idx = nums_idx = 0
	while l_idx < len(l) and r_idx < len(r):
		if l[l_idx] < r[r_idx]:
			nums[nums_idx] = l[l_idx]
			l_idx += 1
		else:
			nums[nums_idx] = r[r_idx]
			r_idx += 1
		nums_idx += 1

	while l_idx < len(l):
		nums[nums_idx] = l[l_idx]
		nums_idx += 1
		l_idx += 1
	while r_idx < len(r):
		nums[nums_idx] = r[r_idx]
		nums_idx += 1
		r_idx += 1		

	return nums	

class Solution:
	def minPairSum(self, nums: List[int]) -> int:
		merge_sort(nums)
		biggest = None
		l = 0
		r = len(nums) - 1
		while l <= r:
			pair = nums[l] + nums[r]
			if biggest is None:
				biggest = pair

			biggest = max(biggest, pair)

			l += 1
			r -= 1
		return biggest
