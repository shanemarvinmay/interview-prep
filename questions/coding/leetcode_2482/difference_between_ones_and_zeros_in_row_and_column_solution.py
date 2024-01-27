class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        # get row and col length
        row_len = len(grid)
        col_len = len(grid[0])
        # get num 1s in rows and col (num 0s can be found be taking len - num of ones)
        row_ones = [0] * row_len
        col_ones = [0] * col_len
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col]:
                    row_ones[row] += 1
                    col_ones[col] += 1
        # calc diff matrix
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                grid[row][col] = row_ones[row] + col_ones[col]
                # Subtracting the number of zeroes in the row
                grid[row][col] -= row_len - row_ones[row]
                # Subtracting the number of zeros in the col 
                grid[row][col] -= col_len - col_ones[col]

        return grid