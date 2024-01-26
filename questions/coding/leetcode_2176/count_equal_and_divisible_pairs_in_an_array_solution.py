from math import gcd
class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        # Attempt 0 O(n^2)
        # pairs = 0
        # num_idxs = dict()

        # for i in range(len(nums)):
        #     num = nums[i]
        #     if num in num_idxs:
        #         num_idxs[num].append(i)
        #     else:
        #         num_idxs[num] = [i]

        # for num in num_idxs:
        #     if len(num_idxs[num]) < 2:
        #         continue
        #     for i in num_idxs[num]:
        #         for j in num_idxs[num]:
        #             if j <= i:
        #                 continue
        #             if i * j % k == 0:
        #                 pairs += 1

        # return pairs

        # Attempt 1 O(x*sqrt(x))
        pairs = 0
        num_idxs = dict()

        for i in range(len(nums)):
            num = nums[i]
            if num in num_idxs:
                num_idxs[num].append(i)
            else:
                num_idxs[num] = [i]

        for num in num_idxs:
            gcd_frequency = dict()
            for idx in num_idxs[num]:
                gcd_i = gcd(idx, k)
                for gcd_j in gcd_frequency:
                    if gcd_i * gcd_j % k == 0:
                        pairs += gcd_frequency[gcd_j]
                if gcd_i in gcd_frequency:
                    gcd_frequency[gcd_i] += 1
                else:
                    gcd_frequency[gcd_i] = 1
        
        return pairs