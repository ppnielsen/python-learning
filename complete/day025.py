'''
Day 25 Cup of Code: numpy & jupyter notebook
numpy array is vector/matrix like, optimized for speed
Lists require for loops which are costly!

Kahn Academy classes:
vector and matrix math
linear algebra
gaussian distribution 1d & 2d
'''

import numpy as np

# list
L = [1, 2, 3]
print('List:', L)

# array
A = np.array([1, 2, 3])
print('Array:', A)


# loop elements
for el in L:
    print(el)

for el in A:
    print(el)

# adding items to list
# can't use these with numpy
L.append(4)
L = L +[5]

print(L)

# summing items in list/array
L2 = []
for i in L:
    L2.append(i + i)

print(L2)

# numpy syntax more simple
A2 = A + A
print(A2)

#multipy lists/arrays
A3 = 2 * A
print('numpy:', A3)

# lists do not perform mathematical operations, they concatenate
L = 2 * L
print('List:', L)


# multiplying elements of list doesn't act as you would think
L4 = []
for el in L:
    L4.append(el * el)
print(L4)

# squaring elements in numpy array
A4 = A**2
print(A4)


# numpy sqrt
A5 = np.sqrt(A)
print(A5)

# numpy log
A6 = np.log(A)
print(A6)

A7 = np.exp(A)
print(A7) # documentation shows that base = 2.718 and A is fed as exponents! Always reference documentation!


