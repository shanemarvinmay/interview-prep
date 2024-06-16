from collections import Counter

class Solution:
	def minSteps(self, s: str, t: str) -> int:
		s_counter = Counter(s)
		t_counter = Counter(t)
		
		total_diff = 0
		
		for ltr in s_counter:
			s_count = s_counter.get(ltr)
			t_count = t_counter.get(ltr, 0)
			total_diff += abs(s_count - t_count)
		for ltr in t_counter:
			if ltr in s_counter:
				continue
			total_diff += t_counter[ltr]

		return total_diff // 2