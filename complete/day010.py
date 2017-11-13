# reverse and input string
x = 'Reverse it!'
b = ('').join(reversed(x))
print(b)

print(x[::-1]) # : = beginning, : = ending, -1 go backwards


# given a number list, output whether it is odd or even
def oddEvenCheck(n):
    oddCnt = 0
    evenCnt = 0
    for i in n: # will work through list
        if i % 2 == 0:
            evenCnt += 1
        else:
            oddCnt += 1
    return f'Event Count: {evenCnt}, Odd Count: {oddCnt}'

nbrList = [123,44,5565,8798,446,65461,3,2,4,86,877]       
print(oddEvenCheck(nbrList))

# given a list print out what the types are
data = [123, True, False, ('hello','bye'),['list','of']]

for i in data:
    print(type(i))

# write a program that prints all number except 3 and 6
for i in range(10):
    if i != 3 and i != 6:
        print(i)

# program a fibonacci seq between 0 and 50. Next number is found by adding 2 number before it
x,y = 0,1
while y < 50:
    print(y)
    x, y = y, x + y

print('\n')


# write a program iterating 0 to 50. if number is a multiple of 3 print SUPAAA.
# if number is a multiple of 5, print BADASS
# if number a multiple of both print SUPA BADASS

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i}: SUPA BADASS!')
    elif i % 3 == 0:
        print(f'{i}: SUPA')
    elif i % 5 == 0:
        print(f'{i}: BAD ASS')
    else:
        print(f'{i}: NONE!')