from typing import List

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        match_map = dict()
        # Making str_map {str: {idxs}}
        str_map = dict()
        for i in range(len(nums)):
            if nums[i] not in str_map:
                str_map[nums[i]] = set()
            str_map[nums[i]].add(i)
        # Finding matches.
        for i in range(len(nums)):
            sub = self.get_sub_str(nums[i], target)
            for idx in str_map.get(sub, set()):
                if i == idx or nums[i] + sub != target:
                    continue
                if i not in match_map:
                    match_map[i] = set()
                match_map[i].add(idx)
        # Count matches.
        matches = 0
        for i, idxs in match_map.items():
            for idx in idxs:
                matches += 1
        return matches

    def get_sub_str(self, num, target):
        if num[0] == target[0]:
            i = 0
            while i < min(len(num), len(target)) and num[i] == target[i]:
                i += 1
            return target[i:]
        if num[-1] == target[-1]:
            i = -1
            while i > max(len(num)*-1, len(target)*-1) and num[i] == target[i]:
                i -= 1
            return target[:i] 
        return ''
