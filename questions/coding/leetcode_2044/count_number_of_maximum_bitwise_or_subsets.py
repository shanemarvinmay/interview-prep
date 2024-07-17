from typing import List
from copy import deepcopy

class Solution:
    def __init__(self):
        self.target = None
        self.combos = None
        self.nums = None
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.nums = nums
        self.target = self.get_or()
        self.combos = []
        self.get_combos(nums)
        return len(self.combos)
    def get_or(self, idxs=None):
        output = 0
        if idxs is not None:
            for idx in idxs:
                output |= self.nums[idx]
            return output
        for num in self.nums:
            output |= num
        return output
    def get_combos(self, nums, idxs=None):
        if idxs is None:
            idxs = set()
        if self.get_or(idxs) == self.target:
            if idxs not in self.combos:
                self.combos.append(deepcopy(idxs))
        for i in range(len(nums)):
            if i in idxs:
                continue
            idxs.add(i)
            self.get_combos(nums, idxs)
            idxs.remove(i)
