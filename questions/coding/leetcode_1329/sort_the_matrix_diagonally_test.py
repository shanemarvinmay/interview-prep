from sort_the_matrix_diagonally_solution import Solution, Coord

import pytest

@pytest.fixture()
def square_matrix():
	return [
		[1,3,3],
		[3,3,2],
		[3,2,2]		
	]
@pytest.fixture()
def wide_matrix():
	return [
		[3,3,1,1],
		[2,2,1,2],
		[1,1,1,2]
	]

@pytest.fixture()
def tall_matrix():
	return [
		[3,3,3],
		[3,2,2],
		[3,2,1],
		[3,2,1]		
	]

@pytest.mark.parametrize("mat, expected", [
	("square_matrix", [
		[1,2,3],
		[2,2,3],
		[3,3,3]
	]),
	("wide_matrix", [
		[1,1,1,1],
		[1,2,2,2],
		[1,2,3,3]
	]),
	("tall_matrix", [
		[1,2,3],
		[1,2,3],
		[2,2,3],
		[3,3,3]
	])
])
def test_diagonal_sort(mat, expected, request):
	solution = Solution()
	mat = request.getfixturevalue(mat)

	solution.diagonalSort(mat)

	assert mat == expected

def test_sort_diagonal(tall_matrix):
	solution = Solution()
	expected = [
		[1,3,3],
		[3,2,2],
		[3,2,3],
		[3,2,1]
	]

	solution.sort_diagonal(tall_matrix, Coord(row=0, col=0))

	assert tall_matrix == expected

@pytest.mark.parametrize("message, mat, start_coord, expected", [
	("Start in bottom corner.", "tall_matrix", Coord(row=3, col=0), Coord(row=3, col=0)),
	("Start in top corner.", "wide_matrix", Coord(row=0, col=0), Coord(row=2, col=2))
])
def test_get_end_of_diagonal(message, mat, start_coord, expected, request):
	solution = Solution()
	mat = request.getfixturevalue(mat)

	got = solution.get_end_of_diagonal(mat, start_coord)

	assert got.row == expected.row, message
	assert got.col == expected.col, message

def test_get_partition(square_matrix):
	solution = Solution()
	expected = Coord(row=1, col=1)
	start = Coord(row=0, col=0)
	end = Coord(row=2, col=2)

	got = solution.get_partition(start, end, square_matrix)

	assert got.row == expected.row
	assert got.col == expected.col