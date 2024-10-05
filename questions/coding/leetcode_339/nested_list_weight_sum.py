from typing import List

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass
    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass
    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass
    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass
    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass

class Solution:
    def depthSum(self, nestedList: List[NestedInteger], depth: int=1) -> int:
        total = 0
        for x in nestedList:
            l = x.getList()
            if l:
                total += self.depthSum(l, depth+1)
                continue
            i = x.getInteger()
            if i:
                total += i * depth
        return total
'''
339. Nested List Weight Sum
https://leetcode.com/problems/nested-list-weight-sum/
'''