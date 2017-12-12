'''
numpy arrays
'''

import numpy as np


# Printing a 5 X 5 array of ones (lists of lists)
x = np.ones((5,5))
print('Normal Array:\n', x)

print() # blank line

# Need to change the rows and columns by indexing!


# From beginning to end, make zero
x[::] = 0
print(x)

x = np.ones((5,5))

# Starting at index two, make all zeros
x[2:] = 0

x = np.ones((5,5))

# start at index 1 and go to end, minus one row and make all zeros
x[1:-1] = 0
print(x)

x = np.ones((5,5))

# start at index 1, go to end, minus 1 and make all zeros for ROW
# start at index 1, go to end, minus 1 and make all zeros for COLUMN
# Think of rows and columns!
x[1:-1, 1:-1] = 0
print(x)




# append to end of an array
x = [10, 15, 25, 63]

x = np.append(x, [[100, 87, 99], [666, 777, 888]])
print(x)

x = np.sort(x)
print(x)



# Create an empty and full array
empty = np.empty([3, 2]) # 3 rows by 2 columns outputting zero in different ways
empty_1 = np.empty((2, 2), dtype=int) # 2 X 2 array outputting only integers
full = np.full((4, 4), 3) # 4 X 4 array filled with 3's

print(empty)
print(empty_1)
print(full)



# script to show which is the fastest at building artificial arrays for future manipulation
from timeit import default_timer as timer

size = 100000000

start = timer()
x = np.full(size, 7)
end = timer()

print('Full:', end-start)

start = timer()
x = np.empty(size, 7)
end = timer()

print('Empty:', end-start)

start = timer()
x = np.zeros(size, 7)
end = timer()

print('Zeros:', end-start)