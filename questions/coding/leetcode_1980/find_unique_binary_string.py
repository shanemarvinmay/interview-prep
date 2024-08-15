from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        for i in range(2 ** n):
            binary = format(i,f'0{n}b')
            print(binary)
            if binary not in nums:
                return binary
# sol = Solution()
# print(sol.findDifferentBinaryString(["01","10"]))
'''
Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
'''