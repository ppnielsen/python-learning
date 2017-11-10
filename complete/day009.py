# create an array of 5 integers and display them by accessing the index

from array import *
array_num = array('i', [3,23,19,86])

print('looped')
for i in array_num:
    print(i)

print('individually')
print(array_num[0])
print(array_num[1])
print(array_num[2])
print(array_num[3])


# append an item to the end of an array
print('Start: ', array_num)
array_num.append(31)
print('End: ', array_num)

# reverse order of array
# :: means to start at the beginning, end at the end, -1 = go backwards
print(array_num[::-1])

# insert a new value before the third item (index position 2) in your array
print(array_num)
array_num.insert(2, 14) # add to the second index number 14
print(array_num)

# remove an item from your array
array_num.pop(3) # if left blank, the last item will be removed
print(array_num)

# remove the first occurrence of an element
new_array = array('i',[1,2,3,4])
print(new_array)
new_array.remove(2) # do not use index!
print(new_array)

# convert array to a list
print(type(new_array))
arr_list = new_array.tolist()
print(type(arr_list))