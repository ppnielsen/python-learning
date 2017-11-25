# make a grid and find out how to move the dots to the right to make it an s
# the same for 'x'... its good practice

letter_s = ''
for row in range(0,7):
    for col in range(0,7):
        if (row == 0 or row == 3 or row == 6) and col > 0 and col < 7:
            letter_s = letter_s + '*'
        elif ( row == 1 or row == 2 ) and col == 1:
            letter_s = letter_s + '*'
        elif ( row == 4 or row == 5 ) and col == 6:
            letter_s = letter_s + '*'
        else:
            letter_s = letter_s + ' '
    letter_s = letter_s + '\n'
print(letter_s)

# program to calculates age in dog years
# dog year 0-2 = 10.5 human years
# after that, each dog year = 4 human years

human = int(input('How old are you?'))
dog = 0

if human < 0:
    print('Age must be a positive integer!')
elif human <= 2:
    dog = human * 10.5
else:
    dog = 21 + ((human - 2) * 4)

print(f'You are {dog} years old in dog years')


# check to see if a letter is a consonant or vowel

x = input('Please enter one letter from the alphabet: ')

if x in ('a','e','i','o','u'):
    print(f'{x} is a vowel')
elif x == 'y':
    print('A, E, I, O, U, and sometimes Y')
else:
    print(f'{x} is a consonant')

# give a month and it'll tell you how many days
thirty = ('April', 'June', 'September', 'November')
thirty_one = ('January','March','May', 'July', 'August','October','December')
mth = input('Please input a month: ')

if mth == 'February':
    print(f'{mth} has 28/29 days')
elif mth in thirty:
    print(f'{mth} has 30 days')
elif mth in thirty_one:
    print(f'{mth} has 31 days')
else:
    print(f'{mth} is not a valid month!')
