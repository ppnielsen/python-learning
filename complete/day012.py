# accept a string and calculate a number of digits
s = input('Type a string: ')
l, d = 0, 0
for char in s:
  if char.isalpha(): # checks if character is alpha
    l = l + 1
  elif char.isdigit(): # checks if character is numeric
    d = d + 1
  else:
    pass

print('Letters: ', l)
print('Digits: ', d)


# check the validity of a password
# at least 1 [a-z], and 1 [A-Z]
# at least 1 number [0-9]
# at least 1 character [$#@]
# no spaces!
# min 6 characters, max 16

import re # regexp matching operations

p = input('Enter password: ')
x = True

while x:
  if( len(p) < 6 or len(p) > 16 ):
    break
  elif not re.search('[a-z]', p):
    break
  elif not re.search('[0-9]', p):
    break
  elif not re.search('[A-Z]', p):
    break
  elif not re.search('[$#@]', p):
    break
  elif re.search('\s', p): # checks for whitespace. if one exists, break code
    break
  else:
    print('Password check is a green light!')
    x = False
    break
if x:
  print('That is a bad password! Never return!')


# find number between 100 and 400 (both included, where each DIGIT is even
# print in csv sequence
even_digits = []
for i in range(100,401):
  s = str(i) # must convert to string because can't find digit of integer
  if ( int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 ):
    even_digits.append(s)
print(even_digits)

# create a program that will print out a pattern of an 'A'
letter_A = ''
for row in range(0,7):
  for col in range(0,7):
    if( ( ( col == 1 or col == 5 ) and row != 0 ) or ( ( row == 0 or row == 3 ) and ( col > 1 and col < 5 ) ) ):
      letter_A = letter_A + '*'
    else:
      letter_A = letter_A + ' ' # have to print a space, otherwise the stars are jumbled together
  letter_A = letter_A + '\n'
print(letter_A)
