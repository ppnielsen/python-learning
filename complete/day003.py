# given an integral number n, create a dictionary with the function that creates the key/value pair
# integral is a number assigned to a function

print('enter in a number')
n = int(input())
d = dict()

for i in range(1, n + 1):
    d[i] = i*i

print(d)
