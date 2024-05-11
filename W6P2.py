def matrix_vector_multiply(matrix, vector):
    num_cols = len(matrix[0])
    if num_cols != len(vector):
        raise ValueError("Make suitable entries")
    result = [0] * len(matrix)
   
    for i in range(len(matrix)):
        for j in range(num_cols):
            result[i] += matrix[i][j] * vector[j]
            
    return result

m = [[1,2],[3,4]]
v = [2,0]
print(matrix_vector_multiply(m,v))
