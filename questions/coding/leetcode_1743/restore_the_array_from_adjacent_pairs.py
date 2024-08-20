from typing import List
from collections import deque

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        nums = []
        map = dict()

        # Mapping pairs.
        for pair in adjacentPairs:
            if pair[0] not in map:
                map[pair[0]] = []
            if pair[1] not in map:
                map[pair[1]] = []
            map[pair[0]].append(pair[1])
            map[pair[1]].append(pair[0])

        # Finding start/end of nums.
        start = None
        for num, neighbors in map.items():
            if len(neighbors) == 1:
                start = num
                break
        
        # Creating nums.
        q = deque([start])
        seen = set()
        while q:
            itr = q.popleft()
            nums.append(itr)
            seen.add(itr)
            for neighbor in map[itr]:
                if neighbor in seen:
                    continue
                q.append(neighbor)
        return nums
