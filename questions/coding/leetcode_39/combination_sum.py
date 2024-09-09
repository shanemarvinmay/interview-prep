from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = []
        def helper(idx, cur, combo):
            if cur == target:
                return combos.append(combo[:])

            for i in range(idx, len(candidates)):
                if cur + candidates[i] <= target:
                    combo.append(candidates[i])
                    helper(i, cur + candidates[i], combo)
                    combo.pop()
        helper(idx=0, cur=0, combo=[])
        return combos
'''
Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
'''
