'''
Day 35 of Cup of Code

What is the missing number?
array 1 is non negative numbers
array 2 is a shuffled version of array 1 and one integer is missing
Which integer is missing?

Could compare second array to first, might also be duplicate elements in array 
this is O(n^2) since nested loop

better to sort first array do binary search O(nlogn)
'''

def finder(arr1, arr2):
    x = list(set(arr1) - set(arr2)) # set is an unordered pair of unique elements. Removes duplicates as well

    return print(x)


finder([1,2,3,4,77,7,5,7], [3,7,2,1,4,6,77,7])

