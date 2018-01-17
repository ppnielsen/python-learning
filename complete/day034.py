'''
Day 34

What is the missing number?
array 1 is non negative numbers
array 2 is a shuffled version of array 1 and one integer is missing
Which integer is missing?

Could compare second array to first, might also be duplicate elements in array 
this is O(n^2) since nested loop

better to sort first array do binary search O(nlogn)
'''

import collections

def finder(arr1, arr2):
    d = collections.defaultdict(int) # adds and creates items in dict if they don't exist. Without this, it would fail

    # creates a key value pair that counts occurrences {1: 1, 6: 1, etc...}
    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))