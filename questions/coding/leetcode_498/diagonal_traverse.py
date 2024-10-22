from typing import List

class Solution:
    def findDiagonalOrder(self, m: List[List[int]]) -> List[int]:
        output = []
        self.m = m
        pos = [0,0]
        end = [len(m),len(m[0])]
        dir = 'up'
        while pos[0] < end[0] or pos[1] < end[1]:
            if not self.is_valid(pos):
                pos = self.get_nxt_diagonal(pos, dir)
                dir = 'up' if dir == 'down' else 'down'
            else:
                output.append(m[pos[0]][pos[1]])
                pos = self.get_nxt(pos, dir)
        return output
    def is_valid(self, pos):
        greater_than_zero = pos[0] >= 0 and pos[1] >= 0
        return greater_than_zero and pos[0] < len(self.m) and pos[1] < len(self.m[0])
    def get_nxt_diagonal(self, pos, dir):
        if dir == 'up':
            if not self.is_valid(pos): pos = [pos[0]+1, pos[1]-1]
            if self.is_valid([pos[0], pos[1]+1]):
                pos = [pos[0], pos[1]+1]
            else:
                pos = [pos[0]+1, pos[1]]
        else:
            if not self.is_valid(pos): pos = [pos[0]-1, pos[1]+1]
            if self.is_valid([pos[0]+1, pos[1]]):
                pos = [pos[0]+1, pos[1]]
            else:
                pos = [pos[0], pos[1]+1]
        return pos
    def get_nxt(self, pos, dir):
        if dir == 'up': return [pos[0]-1, pos[1]+1]
        return [pos[0]+1, pos[1]-1]
'''
498. Diagonal Traverse
https://leetcode.com/problems/diagonal-traverse/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days&difficulty=MEDIUM%2CHARD&status=TO_DO
'''
