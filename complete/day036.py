'''
Day 36

Take an array with positive and negative integers and
find the max RUNNING sum of that array
'''

def largest(arr):
    if len(arr) == 0:
        return print('Too small!')

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)

    return max_sum

print(largest([7,1,2,-1,3,4,10,-12,3,21,-19]))
