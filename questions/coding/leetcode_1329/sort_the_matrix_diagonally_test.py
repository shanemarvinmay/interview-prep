from sort_the_matrix_diagonally_solution import Solution, Coord

import pytest

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

def test_diagonal_sort():
	expected = [
		[1,1,1,1],
		[1,2,2,2],
		[1,2,3,3]
	]
	matrix = [
		[3,3,1,1],
		[2,2,1,2],
		[1,1,1,2]
	]
	solution = Solution()

	solution.diagonalSort(matrix)

	assert matrix == expected

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

