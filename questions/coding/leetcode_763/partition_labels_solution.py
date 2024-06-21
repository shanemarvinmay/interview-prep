from typing import List
class Solution:
	def partitionLabels(self, s: str) -> List[int]:
		groups = self.get_groups(s)
		partitions = self.get_partitions(groups, s)
		# Making the partitions the way their expected on leetcode.
		for i in range(len(partitions)-1, 0, -1):
			partitions[i] = partitions[i] - partitions[i-1]
		return partitions

	def get_groups(self, s):
		groups = []
		ltr_to_group_idx = dict()
		
		for i in range(len(s)):
			ltr = s[i]
			if ltr in ltr_to_group_idx:
				group_idx = ltr_to_group_idx[ltr]
				groups[group_idx][1] = i
			else:
				groups.append([i,i])
				ltr_to_group_idx[ltr] = len(groups) - 1

		return groups
	
	def get_partitions(self, groups, s):
		partitions = []
		group = groups[0]
		for i in range(1, len(groups)):
			next_group = groups[i]
			if next_group[0] > group[1]:
				partitions.append(next_group[0])
				group = next_group
			else:
				group[1] = max(group[1], next_group[1])
		partitions.append(len(s))
		return partitions