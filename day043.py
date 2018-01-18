'''
Cup of Code Day 43
How to find all non-repeat elements in a python array


Non-repeat element
- take a string and return character that never repeats
- if multiple uniques then reutnr on the first unique


* used in several data security scenarios
'''

def non_repeating(s):
    s = s.replace(' ', '').lower()
    char_count = {}
    unique_vals = []

    for c in s:
        if c in char_count:
            char_count[c] += 1
        
        else:
            char_count[c] = 1

    # sorting by the items inside (asc) based on count
    # lambda is a function of itself. Here the key sorts by second part (count)
    y = sorted(char_count.items(), key=lambda x:x[1])
    
    for items in y:
        if item[1] == y[0][1]:
            unique_vals.append(item)
    
    return unique_vals

print(non_repeating('I apple Ape Peels'))