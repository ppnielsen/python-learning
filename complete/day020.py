'''
Day 20 Cup of Code
'''

def max_two(n1, n2):
    '''
    Finds maximum number between two arguments
    '''

    if n1 > n2:
        return n1
    else:
        return n2

def max_three(n1, n2, n3):
    '''
    Finds maximum number between three arguments
    '''

    return max_two(n1, max_two(n2, n3))

# print(max_three(5, -1, 0))


def summing(nbrs):
    '''
    Given tuple, sum all numbers
    '''

    val = 0
    for nbr in nbrs:
        val += nbr
    
    return val

# print(summing((1,2,3,4,100,554)))


def multiply(nbrs):
    val = 1
    for nbr in nbrs:
        val *= nbr
    
    return val

# print(multiply((12,15,16,13,58,6,1)))


def reverse_it(string):
    x = ''
    cnt = len(string)
    while cnt > 0:
        x += string[cnt - 1]
        cnt -= 1
    
    return x

# print(reverse_it('hello world'))