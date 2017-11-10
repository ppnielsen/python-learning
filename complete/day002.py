# Compute factorial of a given number. Result should be printed in a csv single line
# Factorial:5! =*4*3*2*1 = 120

def factorial(nbr):
    if(nbr == 0):
        return 1
    return nbr * factorial(nbr - 1)

print('Enter an integer...')
nbr = int(input())
print(factorial(nbr))
