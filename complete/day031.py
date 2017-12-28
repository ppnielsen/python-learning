'''
Day 31: Cup of Code

Dynamic Arrays question
'''

'''
Given two strings, check to see if they are anagrams. An anagram is when two strings can be written
using the exact same letters.

public relations = crap built on lies

Note: ignore spaces and capitalization!
'''

def anagram(s1, s2):
    # remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # return boolean for sorted match
    return sorted(s1) == sorted(s2)

A = anagram('public relations', 'crap built on lies')
print(A)

# not optimal because it is using a python module... lets do this with count and dictionaries!

def anagram_2(s1, s2):
    # remove spaces and lowercase letters
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # should be same length if true
    if len(s1) != len(s2):
        return False

    # frequency of letters
    count = {}

    for letter in s1:
        if letter in count: # if letter exists in dict
            count[letter] += 1
        else: # if letter doesn't exist in dict
            count[letter] = 1

    # doing opposite to zero out values
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1  

    for k in count:
        if count[k] != 0: # if dict contains anything other than zero, return false
            return False
    
    return True
    


B = anagram_2('philip', 'philip')
print(B)