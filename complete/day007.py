# take two digits, x & y, and create a two-dimensional array

sysIn = input('I need two digits!')

dim = [int(x) for x in sysIn.split(',')]
row = dim[0]
col = dim[1]
list = [[0 for column in range(col)] for rows in range(row)]

for r in range(row):
    for c in range(col):
        list[r][c] = r * c

print(list)