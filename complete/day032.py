'''
Cup of Code day 32
Array Interview Questions

'''

'''
Array Pair Sum
Given an intger array, output all the unique pairs that sum 
up to a specific value k

pair_sum([1,3,2,2], 4)
should return two pairs:
(1,3)
(2,2)
'''

def pair_sum(arr, k):
    if len(arr) < 2:
        return print('List must have at least two values!')

    seen = set() # numbers passed through for loop
    output = set()

    for num in arr:
        target = k - num 

        if target not in seen: # if value needed to equate to k isn't in seen, add it
            seen.add(num)
        else: # if needed value is in seen, append to output
            output.add((min(num, target), max(num, target)))
    
    print('\n'.join(map(str, list(output))))

pair_sum([1,2,4,8,6,5,2,3,7,10], 11)