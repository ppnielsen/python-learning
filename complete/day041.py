'''
Given an array, what is the most frequently occuring element

'''

def most_frequent(list):
    count = {}
    max_count = 0
    max_item = None

    for i in list:
        if i not in count:
            count[i] = 1
        
        else:
            count[i] += 1

        if count[i] > max_count:
            # want max count to reflect the max_count for that particular item in the dict
            max_count = count[i]
            max_item = i
    
    return max_item


print(most_frequent([1,3,3,3,2,1,1,1,-5,-5,-5,-5,-5,-5,-5]))