'''
Day 21 Cup of Code tutorial
Learning numpy
'''

import numpy as np
print(np.__version__)

def one_d_arr():
    '''
    Converting a list of number to 1-d array
    '''
    ls = [1, 1.25, 500, 0.5, 11, -45]
    print('Starting list:', ls)

    # Future use in algorithyms
    one_d = np.array(ls, dtype = int)
    print('My 1-d array:', one_d)

# one_d_arr()

def rect_arr():
    '''
    3x3 matrix (rectangular array) with values ranging from 2 - 10
    '''

    # numpy.arange([start, ]stop, [step, ]dtype = None)
    # step, how many places between numbers
    x = np.arange(2, 11).reshape(3, 3)

    # will output 2-d array (rows and columns)
    # each array is called a vector
    print(x)

    y = np.arange(2, 11, 2)
    print(y)

# rect_arr()


def null_vector():
    '''
    Creating a null vector of size 10
    Then, changes the value of 3 and 6 position to 21
    '''
    
    # how many zeros do you want?
    x = np.zeros(10, dtype=int)
    print(x)

    x[[3, 6]] = 21
    print(x)

# null_vector()


def rev_arr():
    '''
    Reverse an array
    '''

    # range between 7 and 20
    x = np.arange(7,21)
    print(x)

    # :: = from beginning to the end
    # -1 = reverse
    x = x[::-1]
    print(x)

# rev_arr()