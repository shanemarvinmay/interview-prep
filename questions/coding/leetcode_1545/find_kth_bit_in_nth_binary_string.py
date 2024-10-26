class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = self.helper(['0'], n)
        return s[k-1]
    def helper(self, cur, n):
        if n == 0: return cur
        cur += ['1'] + ['1' if i == '0' else '0' for i in cur][::-1]
        return self.helper(cur, n-1)
'''
1545. Find Kth Bit in Nth Binary String
https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/
'''