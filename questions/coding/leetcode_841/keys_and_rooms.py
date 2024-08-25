from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen_keys = set([0])
        keys = deque(rooms[0])
        while keys:
            key = keys.popleft()
            if key in seen_keys: continue
            seen_keys.add(key)
            for new_key in rooms[key]:
                if new_key in seen_keys: continue
                keys.append(new_key)
        return len(seen_keys) == len(rooms)
