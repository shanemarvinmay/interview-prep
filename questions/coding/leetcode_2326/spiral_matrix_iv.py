from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Making the default matrix.
        matrix = []
        for row in range(m):
            matrix.append([])
            for col in range(n):
                matrix[-1].append(-1)
        # Filling in the matrix with the linked list values.
        itr = head
        row_low, row_high = 0, m-1
        col_low, col_high = 0, n-1
        while row_low <= row_high and col_low <= col_high:
            # ->
            row = row_low
            for col in range(col_low, col_high+1):
                if itr is None:
                    return matrix
                matrix[row][col] = itr.val
                itr = itr.next
            row_low += 1
            # |
            # v
            col = col_high
            for row in range(row_low, row_high+1):
                if itr is None:
                    return matrix
                matrix[row][col] = itr.val
                itr = itr.next
            col_high -= 1
            # <-
            row = row_high
            for col in range(col_high, col_low-1, -1):
                if itr is None:
                    return matrix
                matrix[row][col] = itr.val
                itr = itr.next
            row_high -= 1
            # ^
            # |
            col = col_low
            for row in range(row_high, row_low-1, -1):
                if itr is None:
                    return matrix
                matrix[row][col] = itr.val
                itr = itr.next
            col_low += 1
        
        return matrix
