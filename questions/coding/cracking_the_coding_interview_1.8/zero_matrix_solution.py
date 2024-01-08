def set_matrix_col_to_zero(matrix, col):
    for row in range(len(matrix)):
        matrix[row][col] = 0

def set_matrix_row_to_zero(matrix, row):
    for col in range(len(matrix[row])):
        matrix[row][col] = 0

def zero_matrix(matrix):
    zero_rows, zero_cols = [], []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zero_rows.append(row)
                zero_cols.append(col)
                
    for row in zero_rows:
        set_matrix_row_to_zero(matrix, row)
    for col in zero_cols:
        set_matrix_col_to_zero(matrix, col)
                
