from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        self.get_perms(nums, perms)
        return perms

    def get_perms(self, nums, perms, cur_perm=None):
        if cur_perm is None:
            cur_perm = []
        if len(cur_perm) == len(nums):
            perms.append(cur_perm)
            return
        
        for num in nums:
            if num in cur_perm:
                continue
            perm = cur_perm[:]
            perm.append(num)
            self.get_perms(nums, perms, perm)
