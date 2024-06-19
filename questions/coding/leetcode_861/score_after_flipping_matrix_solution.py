from typing import List
class Solution:
	def matrixScore(self, grid: List[List[int]]) -> int:
		biggest = None
		flip_row = True

		while True:
			if flip_row:
				self.flip_rows(grid)
			else:
				self.flip_cols(grid)

			total = self.get_total(grid)

			if biggest and total <= biggest:
				return biggest
			biggest = total
			flip_row = not flip_row

	def flip_cols(self, grid):
		"""Flip bits in col if it results in a hugher num for the col."""
		for col in range(len(grid[0])):
			one_count = self.get_col_count_of_ones(grid, col)
			if one_count <= len(grid) // 2:
				self.flip_col(grid, col)

	def flip_col(self, grid, col):
		for row in range(len(grid)):
			grid[row][col] = 0 if grid[row][col] else 1
	
	def flip_rows(self, grid):
		"""Flip bits in rows if it results in a higher num for the row."""
		for i in range(len(grid)):
			total = self.binary_row_to_decimal(grid[i])
			grid[i] = [0 if i else 1 for i in grid[i]]
			flip_total = self.binary_row_to_decimal(grid[i])
			if total > flip_total:
				grid[i] = [0 if i else 1 for i in grid[i]]

	def binary_row_to_decimal(self, row):
		dec = 0
		ex = 0
		for i in range(len(row)-1, -1, -1):
			dec += row[i] * 2 ** ex
			ex += 1
		return dec

	def get_col_count_of_ones(self, grid, col):
		count = 0
		for row in grid:
			count = count + 1 if row[col] else count
		return count
	
	def get_total(self, grid):
		total = 0
		for row in grid:
			total += self.binary_row_to_decimal(row)
		return total
