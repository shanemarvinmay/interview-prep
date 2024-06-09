from typing import List

class Solution:
    def countTriplets(self, ar: List[int]) -> int:
        triplet_count = 0
        
        for i in range(len(ar) - 1):
            a = 0
            for j in range(i, len(ar) - 1):
                a ^= ar[j]

                b = 0
                for k in range(j+1, len(ar)):
                    b ^= ar[k]
                    if a == b:
                        triplet_count += 1

        return triplet_count