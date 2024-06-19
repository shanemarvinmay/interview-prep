from score_after_flipping_matrix_solution import Solution

import pytest

@pytest.fixture()
def grid():
	return [
		[0,0,1,1],
		[1,0,1,0],
		[1,1,0,0]
		]

def test_matrix_score(grid):
	expected = 39
	solution = Solution()

	got = solution.matrixScore(grid)

	assert got == expected

def test_flip_cols(grid):
	expected = [
		[0,1,1,0],
		[1,1,1,1],
		[1,0,0,1]
	]
	solution = Solution()

	solution.flip_cols(grid)

	assert grid == expected

def test_flip_rows(grid):
	expected = [
		[1,1,0,0],
		[1,0,1,0],
		[1,1,0,0]
	]
	solution = Solution()

	solution.flip_rows(grid)
	
	assert grid == expected

def test_binary_row_to_decimal():
	expected = 10
	row = [1,0,1,0]
	solution = Solution()

	assert solution.binary_row_to_decimal(row) == expected

def test_get_total(grid):
	expected = 25
	solution = Solution()

	assert solution.get_total(grid) == expected

# def test_binary_col_to_decimal(grid):
# 	expected = 1
# 	col = 1
# 	solution = Solution()

# 	got = solution.binary_col_to_decimal(grid, col)

# 	assert got == expected