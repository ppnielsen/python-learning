'''
Day 28 Cup of Code
Big-O theory

'''

# O(1) constant
def f_const(values):
    '''
    Prints first item in a list of values
    '''
    print(values[0])

f_const([1, 2, 3])


# O(n) Linear
# The larger the list grows, the larger the Big-O. This will scale linearly with n
# Computational needs increase with list but not as intensive
def f_lin(lst):
    '''
    Takes list and prints all values
    '''
    for val in lst:
        print(val)

f_lin([1, 2, 3])        

# O(n^2) Quadratic
#  Two lists looped within one another
# for a list of n items, we will have to perform n operations for EVERY item in the list = n ^ 2
# computationally intensive!
def f_quad(lst):
    '''
    Prints pairs for every item in the list
    '''
    for i1 in lst:
        for i2 in lst:
            print(i1, i2)

f_quad([1, 2, 3, 4, 5])

# When it comes to Big O we only care about the most significant terms.
# As the input grows, only fastest growing terms matter



def print_once(lst):
    '''
    Prints all items once
    '''
    for val in lst:
        print(val)

# This would be linear

def print_thrice(lst):
    '''
    Print all items three times
    '''
    for val in lst:
        print(val)
    for val in lst:
        print(val)
    for val in lst:
        print(val)

# operations performed at 3n. Still linear


def comp(lst):
    '''
    this function prints the first item O(1) it is a constant
    then it prints the first 1/2 of the list O(n/2)
    then it print a string 10 times O(n) it is a constant
    '''
    print(lst[0])

    midpoint = len(lst)//2

    for val in lst[:midpoint]:
        print(val)
    
    for x in range(10):
        print('number')

comp([1, 2, 3, 4, 5, 6, 7, 8, 9])
# as n gets larger and larger (scales up), you can easily see how 1 and 10 mean nothing
# and the //2 will begin to have no effect either
# end up with O(n)


# Best case v worst case
# best case = constant: first item in searched list is what we want
# worst case = O(n): search entire list.... linear

# Space Complexity
# concerned with how much memory/space an algorithm uses. the notation of space complexity 
# is the same, but instead of checking the time of operations, we check the size of the allocation of memory

def memory(n=10):
    '''
    Prints hello world n times
    '''
    for x in range(n): # time complexity: O(n)
        print('Memory') # space complexity: O(1) because memory is a constant

memory(10)


