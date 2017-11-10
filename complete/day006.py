import math

# creating a calculator to solve for a variable
c = 50
h = 30
# use: Q = square root(2*c*d/h)

x = []
y = [i for i in input('I need a number: ').split(',')]
for d in y:
    x.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(x))