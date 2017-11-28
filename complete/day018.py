'''
Day 18
'''
def split_it():
    '''
    Splits stuff based on a character
    '''

    x = 'red,white,blue'.split(',')
    print(x)
    print(type(x))

    a, b, c = x

    print(a, b, c)

    words = 'This is a sentence that will be split like a banana'.split(' ')
    print(words)

split_it()

def split_input():
    '''
    Split a user's input
    '''

    print(input('Give me a sentence: ').split(' '))

split_input()

def dicts():
    '''
    Some dictionary stuff
    '''

    d = {1: 'tree', 2: 'house', 3: 'cookies'}

    print('The length of d is:',str(len(d)))
    print(list(d.keys()))
    print(list(d.values()), '\n')

    for k in d:
        print('key:', k)
    
    for k in d:
        print('values:', d[k])
        
dicts()


def dict_order():
    '''
    Dictionary and list ordering... Does it matter?
    '''

    # Order is not important in dictionaries
    d1 = {1: 'tree', 2: 'house', 3: 'cookies'}
    d2 = {1: 'tree', 3: 'cookies', 2: 'house'}
    print('Equal?',d1 == d2)

    # Order is important in lists!
    
    x2 = ['white,red,blue']
    print('Equal?', x1 == x2)

dict_order()

def random_stuff():
    '''
    Showing random module is not just for numbers!
    '''

    import random
    d = {1: 'tree', 2: 'house', 3: 'cookies'}
    l = ['red,white,blue']

    x = random.choice([d])
    y = random.choice([l])

    print('Random with physical dictionary',x)
    print('Random with physical list',y)

    # Random value from hard list
    print(random.choice([1, 'hello', 'why']))

random_stuff()