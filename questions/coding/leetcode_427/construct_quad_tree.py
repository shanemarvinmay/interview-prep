from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        root = Node(
            val=0,
            isLeaf=0,
            topLeft=None,
            topRight=None,
            bottomLeft=None,
            bottomRight=None
        )
        if self.is_all_one_value(grid):
            root.val = self.get_val(grid)
            root.isLeaf = 1
            return root
        tl, tr, bl, br = self.get_corners(grid)
        root.topLeft = self.construct(tl)
        root.topRight = self.construct(tr)
        root.bottomLeft = self.construct(bl)
        root.bottomRight = self.construct(br)
        return root

    def get_corners(self, grid):
        n = len(grid)
        half_way_point = n//2
        top_half = grid[:half_way_point]
        tl, tr = [], []
        for row in top_half:
            tl.append(row[:half_way_point])
            tr.append(row[half_way_point:])
        btm_half = grid[half_way_point:]
        bl, br = [], []
        for row in btm_half:
            bl.append(row[:half_way_point])
            br.append(row[half_way_point:])
        return tl, tr, bl, br

    def is_all_one_value(self, grid):
        cur_val = None
        for row in grid:
            if isinstance(row, list):
                for col in row:
                    if cur_val is None:
                        cur_val = col
                    if cur_val != col:
                        return False
            else:
                if cur_val is None:
                    cur_val = row
                if cur_val != row:
                    return False
        return True
    
    def get_val(self, grid):
        for row in grid:
            if isinstance(row, list):
                for col in row:
                    return col
            return row
