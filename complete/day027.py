'''
Day 27: Cup of Code
Python Algorithms & Big O - Software Engineer Interviews Day 27

Why analyze algorithms?
Procedure/formula for solving a problem
Some are so useful they have names: merge sort, bubble sort, etc.
HOw can we compare the algos to know which is better?
'''

# Imagine I came up with this function
def sum1(n):
    '''
    Take an input of n and return the sum of the numbers from 0 to n
    '''
    final_sum = 0
    for x in range(n+1):
        final_sum += x

    print(final_sum)
    return final_sum

sum1(5)

# then this function...
def sum2(n):
    '''
    Take an input of n and return the sum of the number from 0 to n
    '''
    final_sum = (n*(n+1))/2
    print(final_sum)
    return final_sum

sum2(5)
'''
function sum1 uses a for loop to iteratively add across our range
function sum2 makes use of a formula to solve problem

What to Compare
memory space
time to run - depends of hardware used

Looping is always slower!

The Big O objectively compares the number of assignments each algorithm makes
assignments: in loop, for x in range(n+1) => n+1 assignments

Big-O notation describes how quikcly runtime will grow relative to the input
as the input gets arbitrarily large, i.e. how well it can scale

As n gets arbitrarily large, we only worry about terms that will grow the fastest
as n gets large. Big-O is also known as asymptotic analysis

Asymptotic analysis describes limiting behavior
Which part of the algorithm:
- has the GREATEST effect on the final answer
- is the real bottleneck
- is the limiting factor

Focus on variable calculations!

'''

