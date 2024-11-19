import numpy as np  
from scipy import linalg 

#Calculates the determinant of matrix
A = np.array([[1,2], [3,4]])

print(A) 

print(linalg.det(A))  #Calculates the determinant of the matrix A


#Calculates the inverse of the matrix
B = np.array([[1,3,5], [2,5,1], [2,3,8]])

print(B) 

print(linalg.inv(B))  #Calcultes the inverse of the matrix

print(B.dot(linalg.inv(B))) #For cross-verification i.e., AA(inv) = 1
