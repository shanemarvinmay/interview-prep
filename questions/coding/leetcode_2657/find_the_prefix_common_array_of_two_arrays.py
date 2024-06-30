from typing import List

class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        common = []
        a_set = set()
        b_set = set()

        for i in range(len(a)):
            a_set.add(a[i])
            b_set.add(b[i])

            intersection = a_set.intersection(b_set)

            common.append(len(intersection))
            
        return common