def print_matrix(m):
    print('~~~~~~~~~~~~~~~~~~')
    for row in m:
        for num in row:
            print(num, end=' ')
        print()
    print('~~~~~~~~~~~~~~~~~~')

def move_coords(direction, coords):
    if direction == 'up':
        #  [coords[0] - 1, coords[1]]
        coords[0] -= 1
    elif direction == 'down':
        # [coords[0] + 1, coords[1]]
        coords[0] += 1
    elif direction == 'left':
        # [coords[0], coords[1] - 1]
        coords[1] -= 1
    elif direction == 'right':
        # [coords[0], coords[1] + 1]
        coords[1] += 1
    else:
        raise Exception('Invalid direction')

def rotate_matrix(m):
    # flip vertically
    for row in range(len(m)):
        i, j = 0, len(m[row]) - 1
        while i < j:
            temp = m[row][i]
            m[row][i] = m[row][j]
            m[row][j] = temp
            i += 1
            j -= 1
    # flip x=y line
    i = [0, 0]
    j = [len(m) - 1, len(m) - 1]
    # while coords i and j aren't in the bottom left corner
    while i[0] < len(m) and j[1] >= 0:
        while i != j:
            temp = m[i[0]][i[1]]
            m[i[0]][i[1]] = m[j[0]][j[1]]
            m[j[0]][j[1]] = temp
            move_coords('right', i)
            move_coords('up', j)
        # set i to the begining of the next row down
        move_coords('down', i)
        i[1] = 0
        # set j to the bottom of the next column to the left
        move_coords('left', j)
        j[0] = len(m) - 1
    return m