'''
Cup of Code Day 33 

Interview Questions

What is the missing number?

array 1 is non negative numbers
array 2 is shuffled version of array 1 and one integer is missing

which number is missing?

finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])

Could compare second array to first, might also be duplicate elements in array
This is O(n^2) since nested loop!

Better to sort first array and do binary search O(n log n)
'''

def finder(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2): # zip = tuple unpacking
        if num1 != num2:
            return num1
    
    return arr1[-1]


print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))