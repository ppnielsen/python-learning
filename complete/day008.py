pets = ['dog','cat','bird','rabbit','fish','neighbor']

# print all items, one by one

# individual print statements
print(pets[0])
print(pets[1])
print(pets[2])
print(pets[3])
print(pets[4])
print(pets[5])

# for loop
for pet in pets:
    print(pet)


# conditional statement with a while loop. Ensure that it ends!
acct = 20

while acct < 35:
    print(acct)
    acct += 1
print('Mo money needed!')

# for all number between x and y, which are divisible by 5 and 7
for i in range(1, 3500):
    if i % 7 == 0  and i % 5 == 0:
        print(i)

# guess a random number between 1 and 10

import random

target_num, guess_num = random.randint(1,10), 0
while target_num != guess_num:
    guess_num = int(input('guess a number between 1 and 10. Keep guessing until you are correct!'))
print('game over!')


# create a printed pattern that looks like a sideways triangle

count = 0
for num in range(7):
    count += 1
    print('*' * count)
for num in range(6):
    count -= 1
    print('*' * count)