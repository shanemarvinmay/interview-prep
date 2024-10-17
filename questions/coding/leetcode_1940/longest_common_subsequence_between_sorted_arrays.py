from typing import List

class Solution:
    def longestCommonSubsequence(self, ars: List[List[int]]) -> List[int]:
        output = []
        num_count = [0] * 101
        n = len(ars)

        for ar in ars:
            for num in ar:
                num_count[num] += 1
        
        for num, count in enumerate(num_count):
            if count == n:
                output.append(num)
        
        return output

'''
1940. Longest Common Subsequence Between Sorted Arrays
https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

Constraints:
2 <= arrays.length <= 100
1 <= arrays[i].length <= 100
1 <= arrays[i][j] <= 100
arrays[i] is sorted in strictly increasing order.
'''
