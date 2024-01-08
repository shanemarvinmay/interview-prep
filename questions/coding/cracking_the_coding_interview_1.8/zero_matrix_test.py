from zero_matrix_solution import zero_matrix

def test_zero_matrix():
    matrix = [[0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0]]
    
    zero_matrix(matrix)

    expected_matrix = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],]

    assert matrix == expected_matrix