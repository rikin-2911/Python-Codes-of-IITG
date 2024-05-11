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



import time
import numpy as np 

matrix_size = 1000
vector_size = 1000


matrix = [[np.random.randint(1, 10) for _ in range(vector_size)] for _ in range(matrix_size)]
vector = [[np.random.randint(1,10) for _ in range(vector_size)] for _ in range(matrix_size)]

start_time = time.time()
result_list = matrix_multiply(matrix, vector)
end_time = time.time()
list_time = end_time - start_time
print(f"List implementation time: {list_time:.6f} seconds")

start_time = time.time()
matrix_np = np.array(matrix)
vector_np = np.array(vector)
result_np = matrix_multiply(matrix_np, vector_np)
end_time = time.time()
numpy_time = end_time - start_time
print(f"NumPy implementation time: {numpy_time:.6f} seconds")

assert np.array_equal(result_list, result_np)
print("Results are the same")
