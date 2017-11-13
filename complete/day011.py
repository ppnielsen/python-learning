# take 2 digits m,n as inputs and generate a 2-d array
# the element value in the i-th row and j-th col should be i * j
row_num = 3
col_num = 4
list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        list[row][col] = row * col

print(list, '\n')


# accept a list of all lowercase and output to ALL CAPS
all_caps = []
while True:
    l = input('give me lowercase!')
    if l:
        all_caps.append(l.upper())
    else: # will break if user doesn't input any thing and presses enter!
        break;
for i in all_caps:
    print(i)


# write a program that accepts cs 4 digit binary numbers as its input
# and print the number that are divisible by 5 in a cs seq
def div_binary():
    s = input('Give me binaries!: ')
    l = s.split(',')
    for i in l:
        if int(str(i), 2) % 5 == 0: # second argument is the base, for binaries, you want base 2
            print(f'Output: {i}')

div_binary()
