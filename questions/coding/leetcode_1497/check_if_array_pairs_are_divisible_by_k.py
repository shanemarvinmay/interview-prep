from typing import List

class Solution:
    def canArrange(self, nums: List[int], k: int) -> bool:
        # Making mod map.
        # { num%k: {idx, idx}}
        mod_map = dict()
        for i in range(len(nums)):
            mod = nums[i] % k
            if mod not in mod_map:
                mod_map[mod] = set()
            mod_map[mod].add(i)
        # Checking to make sure each num belongs to a pair.
        visited = set()
        for i in range(len(nums)):
            if i in visited: continue
            # Returning true if mod_map is empty,
            # since this means every num was placed in a pair.
            if not mod_map:
                return True
            mod = nums[i] % k
            if mod == 0:
                target = 0  
            else:
                target = k - mod
            mod_set = mod_map.get(mod, set())
            target_set = mod_map.get(target, set())
            if mod == target and len(mod_set) < 2:
                return False
            elif len(mod_set) == 0 or len(target_set) == 0:
                return False
            visited.add(i)
            mod_set.remove(i)
            visited.add(target_set.pop())
            if len(mod_set) == 0 and mod in mod_map:
                del mod_map[mod]
            if len(target_set) == 0 and target in mod_map:
                del mod_map[target]
        return len(list(mod_map.keys())) == 0
