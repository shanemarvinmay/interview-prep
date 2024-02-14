from collections import namedtuple
Coord = namedtuple('coord', ['row', 'col'])
class Solution:
    def coord_is_in_range(self, coord, mat):
        '''Returns True if coord is not out of range of matrix.'''
        return coord[0] < len(mat) and coord[1] < len(mat[0])

    def diagonalSort(self, mat: list[list[int]], start_coord=None) -> list[list[int]]:
        '''Break apart mat rows to do merge sort. Then when bringing them
        together, sort by every diagonal.
        '''
        if len(mat) < 2:
            return
        start_coord = Coord(row=0, col=0) if start_coord is None else start_coord
        mid = len(mat) // 2
        left = mat[:mid]
        right = mat[mid]
        self.diagonalSort(left, start_coord)
        self.diagonalSort(right, Coord(row=mid, col=0))

        # Sort every diagonal line
        mat_coord = start_coord
        for col in range(len(left)):
            left_coord = Coord(row=0, col=col)
            # right's col must always be the next number in the diagonal
            right_coord = Coord(row=0, col=col+len(left))
            while self.coord_is_in_range(left_coord, left) and self.coord_is_in_range(right_coord, right):
                if left[left_coord.row, left_coord.col] < right[right_coord.row, right_coord.col]:
                    mat[mat_coord.row][mat_coord.col] = left[left_coord.row, left_coord.col]
                    left_coord = Coord(row=left_coord.row + 1, col=left_coord.col + 1)
                else:
                    mat[mat_coord.row][mat_coord.col] = right[right_coord.row, right_coord.col]
                    right_coord = Coord(row=right_coord.row + 1, col=right_coord.col + 1)
                mat_coord = Coord(row=mat_coord.row + 1, col=mat_coord.col + 1)
        
            # Add the leftovers
            while self.coord_is_in_range(left_coord, left):
                mat[mat_coord.row][mat_coord.col] = left[left_coord.row, left_coord.col]
                left_coord = Coord(row=left_coord.row + 1, col=left_coord.col + 1)
                mat_coord = Coord(row=mat_coord.row + 1, col=mat_coord.col + 1)
            # for right
            while self.coord_is_in_range(right_coord, right):
                mat[mat_coord.row][mat_coord.col] = right[right_coord.row, right_coord.col]
                right_coord = Coord(row=right_coord.row + 1, col=right_coord.col + 1)
                mat_coord = Coord(row=mat_coord.row + 1, col=mat_coord.col + 1)
        
        return mat