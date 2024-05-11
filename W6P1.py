def vector_dot_product(a,b):
    if len(a) != len(b):
        raise ValueError("Vectors must have the same length")
    dot_product = 0
    for i in range(len(a)):
        dot_product += a[i] * b[i]
    return  dot_product    
# Example
c = [1, 848, 3]
d = [2, 3, 4]
print(vector_dot_product(c,d))