# Find all number that are between 2000 and 3200 that are divisible by 7 but not by 5

# Holds values
EMPTY = []

# Iterate through range of numbers
for i in range(2000, 2100): # 3201 not included!
    if (i % 7 == 0) and (i % 5 != 0):
        EMPTY.append(str(i))

# Print comma delimited list
print(','.join(EMPTY))
