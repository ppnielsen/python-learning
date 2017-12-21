'''
Day 26: numpy
Crash Course pt 2
Matrix is a 2d array and mathematical object containing numbers
Vector is a 1d mathematical object containing numbers
'''

import numpy as np

a = np.array([1, 3])
b = np.array([2, 4])

# matrix multiplication
# matrix is row, column!
'''
When you transpose b:

1 x 2 = 2
3 x 4 = 12

14
'''
x1 = np.dot(a, b)
print(x1)


# comparing operations of lists and numpy arrays
# l is a list of lists
# m is a matrix

l = [[1, 2], [3, 4]]
m = np.array([[1, 2], [3, 4]])

# retrieving specific elements
print(l[0])
print(l[0][0])

print(m[0][0]) # functions same as list in this regard (first element retrieved)

print(m[0, 0]) # doesn't work with lists!

# numpy's documentation says do not use matrix even though it is available within module!

# transposes the matrix
# row of original matrix becomes column of new matrix

print('Original matrix:', m)
print('Transposed matrix:', m.T) # used for various mathematical operations


# dummy arrays to work with
z = np.zeros(10, dtype=int)
print(z)

p = np.zeros((10, 10), dtype=int)
print(p)

# uniformly distributed number from 0 to 1
random_matrix = np.random.random((10,10))
print(random_matrix)

# mean and variances
arr.mean()
arr.var()