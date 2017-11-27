'''
Day 15 of Cup of Code's Python tutorial
'''

def sum_avg():
    '''
    Given a list of numbers, find the sum and average
    '''
    print('I need some integers! Enter 0 to finish your list.')

    cnt = 0
    summed = 0
    nbr = 1

    while nbr != 0:
        nbr = int(input(''))
        summed = summed + nbr
        cnt += 1

    if cnt == 0:
        print('I neeeeeeed numbers!')
    else:
        print('sum and average are:', summed, summed/(cnt - 1))

# sum_avg()

def mult_tbl():
    '''
    Creating a multiplication table
    '''

    chosen = int(input('What number should we create a table for? '))
    for i in range(13):
        print(chosen, 'x', i, '=', chosen * i)

# mult_tbl()

def nbr_numerical_val():
    '''
    prints a number and its numerical characters
    '''
    for i in range(10):
        print('$' * i)

# nbr_numerical_val()
