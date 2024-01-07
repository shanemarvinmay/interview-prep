from rotate_matrix_solution import move_coords, rotate_matrix

def test_move_coords_up():
    coords = [1, 1]
    
    move_coords('up', coords)

    assert coords == [0, 1]

def test_move_coords_right():
    coords = [1, 1]
    
    move_coords('right', coords)

    assert coords == [1, 2]

def test_move_coords_down():
    coords = [1, 1]
    
    move_coords('down', coords)

    assert coords == [2, 1]

def test_move_coords_left():
    coords = [1, 1]
    
    move_coords('left', coords)

    assert coords == [1, 0]


def test_rotate_matrix_odd_length():
    m = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]

    rotate_matrix(m)

    expected_m = [
        [6, 3, 0],
        [7, 4, 1],
        [8, 5, 2]
    ]

    assert m == expected_m

def test_rotate_matrix_even_length():
    m = [
        [0, 1],
        [2, 3]
    ]

    rotate_matrix(m)

    expected_m = [
        [2, 0],
        [3, 1]
    ]

    assert m == expected_m