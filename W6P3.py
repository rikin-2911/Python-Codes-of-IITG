def matrix_multiply(matrix1, matrix2):
    rows_mat1 = len(matrix1)
    cols_mat1 = len(matrix1[0])
    rows_mat2 = len(matrix2)
    cols_mat2 = len(matrix2[0])
    if cols_mat1 != rows_mat2:
        raise ValueError("Please enter appropriate entries!")
    result_mat = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):
                result_mat[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_mat

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_multiply(matrix1, matrix2)
print(result)           
