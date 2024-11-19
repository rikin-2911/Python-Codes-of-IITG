import numpy as np   

""" Numpy 1-D array """
arr1d = np.array([1,2,3,4,5])
print(arr1d)

#Accessing elements (Index start's from '0')
print(arr1d[2])

#Modify the elements
arr1d[0] = 10

print(arr1d)

""" Numpy 2-D array """
arr2d = np.array([[1,2,3], [4,5,6]])
print(arr2d)

print(arr2d[1,2])

arr2d[1,1] = 20 

print(arr2d)

""" Numpy array objects """
array_ex = np.array([[[0,1,2,3],
                      [4,5,6,7]],
                      
                      [[0,1,2,3],
                       [4,5,6,7]],

                       [[0,1,2,3],
                        [4,5,6,7]],
                        ])

print(array_ex)


"""Numpy array objects"""

ones = np.ones((5,5))
print(ones) 

zeros = np.zeros((5,5))
print(zeros)

rn = np.random.default_rng() #for generating random number using Numpy
x = rn.random(3)
print(x)
