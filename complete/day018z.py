'''
Cup of Code tutorial 18 part 2
'''

def arg_vector():
    '''
    Using argument vector. Allows you to run script from command line and
    pass values without using input
    '''

    from sys import argv

    # Similar to user input
    script, first, second, third = argv

    print('The script is:', script)
    print('The first variable is:', first)
    print('The second variable is:', second)
    print('The third variable is:', third)



arg_vector()
