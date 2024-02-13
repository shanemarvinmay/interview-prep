from collections import namedtuple

class Solution:
    def diagonal_merge_sort(self, mat):
        '''Break apart mat rows to do merge sort. Then when bringing them
        together, sort by every diagonal.
        '''
        if len(mat) < 2:
            return
        Coord = namedtuple('coord', ['row', 'col'])
        mid = len(mat) // 2
        left = mat[:mid]
        right = mat[mid]
        self.diagonal_merge_sort(left)
        self.diagonal_merge_sort(right)

        # Sort every diagonal line
        mat_coord = Coord(row=0, col=0)
        left_end_cord = Coord(row=len(left), col=len(left[0]))
        right_end_cord = Coord(row=len(right), col=len(right[0]))
        for col in range(len(left)):
            left_coord = Coord(row=0, col=col)
            # right's col must always be one more than
            right_coord = Coord(row=0, col=1)
            while left_coord < left_end_cord and right_coord < right_end_cord:
                if left[left_coord.row, left_coord.col] < right[right_coord.row, right_coord.col]:
                    mat[mat_coord.row][mat_coord.col] = left[left_coord.row, left_coord.col]
                    left_coord = Coord(row=left_coord.row + 1, col=left_coord.col + 1)
                else:
                    mat[mat_coord.row][mat_coord.col] = right[right_coord.row, right_coord.col]
                    right_coord = Coord(row=right_coord.row + 1, col=right_coord.col + 1)
                mat_coord = Coord(row=mat_coord.row + 1, col=mat_coord.col + 1)
        
        # Add the leftovers
        # for left
        # for right
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        '''TODO: put merge sort code here (you don't need the extra function).'''
        pass